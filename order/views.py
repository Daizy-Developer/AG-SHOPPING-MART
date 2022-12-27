from django.shortcuts import render,redirect,HttpResponse
from cart.cart import Cart
from .models import OrderItem ,Order
from .forms import OrderCreateForm
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect
# from django.contrib.auth.decorators import login_required
@ensure_csrf_cookie
@csrf_protect
def order_create(request):
    cart = Cart(request)
    form = OrderCreateForm()  # define form here
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)  # update form if the request method is POST
            if form.is_valid():
                form.instance.Account = request.user
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(order=order, product=item['product'],
                    price=item['price'], quantity=item['quantity'])
                    cart.clear()
                    return render(request, 'order/created.html', {'order': order,'form': form })
            else:
                form.instance.Account = request.user
                
            return render(request, 'order/create.html', {'cart': cart,'form': form})
    else:
        return redirect('/login')
    return render(request, 'order/create.html', {'cart': cart,'form': form})


def Orders(request):
    order_history = Order.objects.filter(Account=request.user) 
    orders = OrderItem.objects.filter(order__in=order_history)
        
    return render(request, 'order/orders.html',{"order_history":order_history,"orders":orders})

# def Orders(request):
#     order_history = Order.objects.filter(Account=request.user) 
#     orders =  OrderItem.objects.filter(order=order_history)
#     print(orders)
#     return render(request, 'order/orders.html',{"order_history":order_history,"orders":orders})
