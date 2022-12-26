from django.shortcuts import render, get_object_or_404,redirect
from cart.forms import CartAddProductForm
from .models import Category, Product
# Authentication
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect
@ensure_csrf_cookie
@csrf_protect
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'shop/product/list.html', context)

# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     context = {'category': category, 'categories': categories, 'products': products}
#     return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'shop/product/detail.html', context)


def Login(request):
        if request.method=='POST':
            USR_NAME = request.POST['username']
            PASSWORD = request.POST['password']
            USR = authenticate(username=USR_NAME,password= PASSWORD)
            if USR is not None:
                login(request,USR)
                return redirect('/')
                
            
            return render(request,"others/login.html")
        if request.user.is_authenticated:
            return redirect('/')
        return render(request,"others/login.html")

def USR_Logout(request):
    logout(request)
    return redirect('/')