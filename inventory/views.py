from django.shortcuts import render, redirect, get_object_or_404  # 添加导入
from django.contrib.auth import authenticate, login, logout
from .models import Product
from .forms import ProductForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            return render(request, 'login.html', {'error': '无效的凭证'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def product_list(request):
    products = Product.objects.filter(owner=request.user)
    return render(request, 'index.html', {'products': products})

from django.contrib.auth.decorators import login_required

@login_required
def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'upload.html', {'form': form})


def edit_product(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    
    product = get_object_or_404(Product, id=pk, owner=request.user)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'edit.html', {'form': form})

def delete_product(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    
    product = get_object_or_404(Product, id=pk, owner=request.user)
    product.delete()
    return redirect('product_list')


def tobacco_list(request):
    products = Product.objects.filter(category='tobacco')  # 确保分类标识符正确
    return render(request, 'tobacco.html', {'products': products})

def liquor_list(request):
    products = Product.objects.filter(category='liquor')  # 确保分类标识符正确
    return render(request, 'liquor.html', {'products': products})
