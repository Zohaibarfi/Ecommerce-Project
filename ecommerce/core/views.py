from django.shortcuts import render, redirect

from django.http import HttpResponse


from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from core.models import CartItem 

# Create your views here.


def index(request):
    products = Product.objects.all()
    vendors = Vendor.objects.all()
    
    
    context = {
        "products" : products,
        "vendors" : vendors
    }
    return render(request, 'core/index.html', context)


def shop(request):
    
    return render(request, 'core/shop.html')

def about(request):
    return render(request, 'core/about.html')

def blog(request):
    return render(request, 'core/blog.html')

def contact(request):
    
    return render(request, 'core/contact.html')

#def cart(request):
 #   return render(request, 'core/cart.html')




@login_required

def cart(request):
    # Get or create an active cart order for the current user
    cart_order, created = CartOrder.objects.get_or_create(user=request.user, paid_status=False)
    
    # Get all items in the cart
    cart_items = CartOrderItems.objects.filter(order=cart_order)
    
    # Calculate the subtotal for each item and the total cart value
    for item in cart_items:
        item.subtotal = item.qty * item.product.price
    total = sum(item.subtotal for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'core/cart.html', context)


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_order, created = CartOrder.objects.get_or_create(user=request.user, paid_status=False)
    cart_item, created = CartOrderItems.objects.get_or_create(order=cart_order, product=product)
    
    if not created:
        cart_item.qty += 1
        cart_item.save()
    
    return redirect('core:cart')


def remove_from_cart(request, item_id):
    try:
        cart_order = CartOrder.objects.get(user=request.user, paid_status=False)
        cart_item = CartOrderItems.objects.get(order=cart_order, id=item_id)
        cart_item.delete()
    except CartOrder.DoesNotExist:
        pass  # Handle the case where the cart doesn't exist
    except CartOrderItems.DoesNotExist:
        pass  # Handle the case where the cart item doesn't exist

    return redirect('core:cart')




def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:index')
    else:
        form = UserCreationForm()
    return render(request, 'core/sign-up.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('core:index')
    else:
        form = AuthenticationForm()
    return render(request, 'core/sign-in.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('core:index')

def profile(request):
    return render(request, 'core/profile.html') 


@login_required
def checkout(request):
    if request.method == 'POST':
        payment_method = request.POST.get('paymentMethod')
        if payment_method == 'online':
            return render(request, 'core/payment.html')
        else:
            # Handle cash on delivery
            # Save order details to the database
            return HttpResponse('Your order has been placed.')
    else:
        return render(request, 'core/checkout.html')
    
    
def payment_completed_view(request):
    return render(request, 'core/payment-completed.html')

def payment_failed_view(request):
    return render(request, 'core/payment-failed.html')
    
    

    
    
    
    