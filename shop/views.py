from django.shortcuts import render, get_object_or_404,redirect
from cart.forms import CartAddProductForm
from .models import Category, Product ,Home_Slider,Block_Buster_Deal
# Authentication
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect

# Registration
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .forms import UserRegisterForm , ContactUsForm

def home(request):
    Slider_Img  =  Home_Slider.objects.all()
    Blockbuster =  Block_Buster_Deal.objects.all()
    products_details = Product.objects.filter(id__in=Blockbuster.values("Item"))
    # products_details = Product.objects.filter(id__in=[i.Item for i in Block_Buster_Deal.objects.all()])
    # products_details = Block_Buster_Deal.objects.filter(Item__in=[i.id for i in Product.objects.filter()])

    print(products_details)
    return render(request,"shop/home.html",{"slider":Slider_Img,"products":products_details})

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


def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('/login')
    else:
        form = UserRegisterForm()
    return render(request, 'others/register.html', {'form': form, 'title':'register here'})

def Contact(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            # form.save()
            complains = form.save()
            print(complains.id)
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return render(request,'others/Complain.html',{"form":complains})
    
    else:
        return render(request, 'others/contact.html',{"form":form})


def About(request):
    return render(request,"others/About.html")
def USR_Logout(request):
    logout(request)
    return redirect('/')

