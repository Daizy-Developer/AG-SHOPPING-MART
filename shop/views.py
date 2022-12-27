from django.shortcuts import render, get_object_or_404,redirect
from cart.forms import CartAddProductForm
from .models import Category, Product
# Authentication
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect

# Registration
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
  

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


def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # ######################### mail system ####################################
            # htmly = get_template('others/Email.html')
            # d = { 'username': username }
            # subject, from_email, to = 'welcome', 'thesample786@gmail.com', email
            # html_content = htmly.render(d)
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('/login')
    else:
        form = UserRegisterForm()
    return render(request, 'others/register.html', {'form': form, 'title':'register here'})

def USR_Logout(request):
    logout(request)
    return redirect('/')