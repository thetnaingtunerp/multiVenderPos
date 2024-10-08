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
    
    
    path('homeview/', homeview.as_view(), name='homeview'),
    path('dashboard/<int:id>/', dashboard.as_view(), name='dashboard'),

    path('categoryview/', categoryview.as_view(), name='categoryview'),
    path('category/delete/<int:id>/', categorydelete.as_view(), name='categorydelete'),
    path('product_list_by_category/<int:id>/', product_list_by_category.as_view(), name='product_list_by_category'),
]