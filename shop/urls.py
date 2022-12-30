from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='product_list'),
    path('shop', views.product_list, name='product_list'),
    path('login', views.Login, name='login'),
    path('register', views.Register, name='login'),
    path('logout', views.USR_Logout, name='logout'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('contact', views.Contact, name='contact'),
    path('abt-us', views.About),
    # path('complain', views.complain),
    

]