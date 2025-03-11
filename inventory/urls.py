from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # 主页路由
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('upload/', views.upload_product, name='upload_product'),
    # 新增以下两条路由
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('tobacco/', views.tobacco_list, name='tobacco_list'),
    path('liquor/', views.liquor_list, name='liquor_list'),
]