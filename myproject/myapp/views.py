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

def test(request):
    return render(request, 'base.html')

def authlogin(request):
    return render(request, 'auth-login.html')



class categoryview(View):
    def get(self,request):
        br = branch.objects.get(usr=request.user)
        categories = category.objects.filter(branch=br.id)
        context = {'categories':categories}
        return render(request, 'categoryview.html', context)

    def post(self, request):
        cat = request.POST.get('category')
        br = branch.objects.get(usr=request.user)
        brid = int(br.id)
        c = category(branch=br, usr=request.user, category=cat)
        c.save()
        return redirect(request.META['HTTP_REFERER'])
    
class categorydelete(View):
    def get(self, request, id):
        task = get_object_or_404(category, id=id)
        task.delete()
        return JsonResponse({'status':'success'})