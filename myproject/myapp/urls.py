from django.urls import path
from .views import *
from . import views
app_name = 'myapp'
urlpatterns = [
    path('test/',views.test, name='test'),
    path('authlogin/', views.authlogin, name='authlogin'),

    path('login/', UserLoginView.as_view(), name = 'UserLoginView'),
    path('logout/', UserLogoutView.as_view(), name='UserLogoutView'),
    path('AdminUserLoginView/', AdminUserLoginView.as_view(), name='AdminUserLoginView'),
    
    
    path('', homeview.as_view(), name='homeview'),
    path('dashboard/<int:id>/', dashboard.as_view(), name='dashboard'),

    path('categoryview/', categoryview.as_view(), name='categoryview'),
    path('category/delete/<int:id>/', categorydelete.as_view(), name='categorydelete'),
    path('category/edit/<int:id>/', categoryedit.as_view(), name='categoryedit'),
    path('product_list_by_category/<int:id>/', product_list_by_category.as_view(), name='product_list_by_category'),

    path('productview/', productview.as_view(), name='productview'),
    path('saleview/', saleview.as_view(), name='saleview'),
    path('addtocart/', addtocart.as_view(), name='addtocart'),
    path('invoicesave/', invoicesave.as_view(), name='invoicesave'),
    path('invcustomername/', invcustomername.as_view(), name='invcustomername'),
    
    path('salereportview/', salereportview.as_view(), name='salereportview'),
    
]