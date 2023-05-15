from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/',views.index, name='index'),
    path('home/',views.home, name='home'),
    path('',auth_views.LoginView.as_view(template_name='products/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='products/logout.html'), name='logout'),
    path('index/<int:product_id>', views.product_detail, name='product_detail'),
    path('issued_item/<str:pk>/', views.issued_item, name='issued_item'),
    path('reciept', views.reciept, name='reciept'),#handle a reciept after a suuccessful sale
    path('add_to_stock/<str:pk>/', views.add_to_stock, name='add_to_stock'),
    path('all_sales/<int:user_id>/', views.all_sales, name='all_sales'),#handles all all_sales from the browser
    # path('reciept/<int:reciept_id>/', views.reciept_detail, name='reciept_detail'),
    path('reciept/<int:reciept_id>', views.reciept_detail, name='reciept_detail'),
    path('delete_item/<int:product_id>', views.delete_item, name='delete_item'),
]