from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('shipping_info/', views.shipping_info, name='shipping_info'),
    path('billing/', views.billing, name='billing'),

]