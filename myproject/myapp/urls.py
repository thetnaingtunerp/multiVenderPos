from django.urls import path
from .views import *
from . import views
app_name = 'myapp'
urlpatterns = [
    path('test/',views.test, name='test'),
    path('login/', views.authlogin, name='authlogin'),
    path('categoryview/', categoryview.as_view(), name='categoryview'),
    path('categorydelete/<int:id>/', categorydelete.as_view(), name='categorydelete'),
]