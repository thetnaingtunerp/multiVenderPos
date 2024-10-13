import datetime

from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum,Count,F
from django.http import HttpResponse
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.paginator import Paginator

from .models import *
from .forms import *

def test(request):
    return render(request, 'base.html')

def authlogin(request):
    return render(request, 'auth-login.html')



class UserRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('myapp:UserLoginView')
        return super().dispatch(request, *args, **kwargs)


class SuperUserRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated & request.user.is_superuser:
            pass
        else:
            return redirect('myapp:UserLoginView')
        return super().dispatch(request, *args, **kwargs)


class AdminUserLoginView(FormView):
    template_name = 'adminlogin.html'
    form_class = AdminLoginForm
    success_url = reverse_lazy('myapp:homeview')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data['password']
        usr = authenticate(username=username, password=password)

        if usr is not None:
            login(self.request, usr)

        else:
            return render(self.request, self.template_name, {'form': self.form_class, 'error': 'Invalid user login!'})
        return super().form_valid(form)




class UserLoginView(FormView):
    template_name = 'login.html'
    form_class = ULoginForm
    success_url = reverse_lazy('myapp:homeview')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data['password']
        usr = authenticate(username=username, password=password)

        if usr is not None:
            login(self.request, usr)

        else:
            return render(self.request, self.template_name, {'form': self.form_class, 'error': 'Invalid user login!'})
        return super().form_valid(form)

class UserLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('myapp:UserLoginView')




# ===================================== start Home ========================================

class homeview(UserRequiredMixin,View):
    def get(self, request):
        br = branch.objects.filter(usr=request.user)
        context = {'br':br}
        return render(request, 'homeview.html', context)

class dashboard(View):
    def get(self, request, id):
        br = branch.objects.filter(usr=request.user, id=id)
        brname = branch.objects.get(id=id)
        branch_id = self.request.session.get("branch_id", None)
        if branch_id:
            self.request.session['branch_id'] = id
            self.request.session['branch_name'] = brname.branch_name
            products = product.objects.filter(branch=branch_id)
            categories = category.objects.filter(branch=id)
        # print(branch_id)
            context = {'br':br, 'products':products, 'categories':categories}
            # return render(request, 'dashboard.html', context)
            return redirect('myapp:saleview')
            
        else:
            self.request.session['branch_id'] = id
            self.request.session['branch_name'] = brname.branch_name
            
            products = product.objects.filter(branch=branch_id)
            categories = category.objects.filter(branch=id)
        # print(branch_id)
            context = {'br':br, 'products':products, 'categories':categories}
            return render(request, 'dashboard.html', context)
# ===================================== end Home ========================================



# ===================================== start category ========================================

class categoryview(View):
    def get(self,request):
        try:
            branch_id = self.request.session.get("branch_id", None)
            br = branch.objects.get(usr=request.user, id=branch_id)
            categories = category.objects.filter(branch=br.id)
            context = {'categories':categories}
            return render(request, 'categoryview.html', context)
        except:
            return redirect('myapp:homeview')
        

    def post(self, request):
        cat = request.POST.get('category')
        branch_id = self.request.session.get("branch_id", None)
        br = branch.objects.get(usr=request.user, id = branch_id)
        # brid = int(br.id)
        
        c = category(branch=br, usr=request.user, category=cat)
        c.save()
        return redirect(request.META['HTTP_REFERER'])
    
    def put(self,request):
        print('PUT')
        return redirect(request.META['HTTP_REFERER'])
    
class categorydelete(View):
    def get(self, request, id):
        task = get_object_or_404(category, id=id)
        task.delete()
        return JsonResponse({'status':'success'})

class categoryedit(View):
    def get(self, request, id):
        catname = request.GET.get('cat')
        ca = category.objects.filter(id=id)
        ca.update(category=catname)
        return JsonResponse({'status':'success'})

class product_list_by_category(View):
    def get(self, request, id):
        try:
            branch_id = self.request.session.get("branch_id", None)
            catauth = category.objects.get(usr=request.user, branch=branch_id, id=id)
            if branch_id is not None and catauth.id == id:
                cat = get_object_or_404(category, id=id)
                products = product.objects.filter(category=cat)
                fm = itemcreateform()
                context = {'products':products, 'cat':cat, 'fm':fm}
                return render(request, 'product_list_by_category.html', context)
        except:
            return redirect('myapp:homeview')
        
    
    def post(self, request, id):
        try:
            name = request.POST.get('name')
            saleprice = request.POST.get('saleprice')
            purchaseprice = request.POST.get('purchaseprice')
            branch_id = self.request.session.get("branch_id", None)
            catauth = category.objects.get(usr=request.user, branch=branch_id, id=id)
            br = branch.objects.get(usr=request.user, id = branch_id)

            if branch_id is not None and catauth.id == id:
                p=product(branch=br, name=name, category=catauth, saleprice=saleprice, purchaseprice=purchaseprice)
                p.save()
                return redirect(request.META['HTTP_REFERER'])
        except:
            return redirect('myapp:homeview')
        
        
        

# ===================================== end category ========================================

# ===================================== start product ========================================

class productview(View):
    def get(self, request):
        try:
            branch_id = self.request.session.get("branch_id", None)
            if branch_id is not None:
                products = product.objects.filter(branch=branch_id)
                fm = itemcreateform()
                context = {'products':products, 'fm':fm}
                return render(request, 'productview.html', context)
            else:
                return redirect('myapp:homeview')
        except:
            return redirect('myapp:homeview')
        





# ===================================== end product ========================================

class saleview(View):
    def get(self, request):
        try:
            branch_id = self.request.session.get("branch_id", None)
            products = product.objects.filter(branch=branch_id)
            context = {'products':products}
            return render(request, 'saleview.html', context)
        except:
            return redirect('myapp:homeview')


class addtocart(View):
    def get(self, request):
        cid = request.GET.get('cid')
        pqty = request.GET.get('pqty')
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            print(cart_id)
        else:
            print('no card id')
        return JsonResponse({'status':'success'})



# ===================================== end sale ========================================