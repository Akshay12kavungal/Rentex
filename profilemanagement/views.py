from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from renting.models import ActionCamera, AudioVisualEquipment, Camera, CampingGear, CreatorGear, GamingConsole, RidingGear, TrekkingGear, WinterWear
from .models import Wallet, Order, CartItem
from .forms import CustomerForm, LoginForm, RentalForm, UserForm, WalletForm, OrderForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType




def signup_customer(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        customer_form = CustomerForm(request.POST, request.FILES)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('login_customer')
    else:
        user_form = UserForm()
        customer_form = CustomerForm()
    return render(request, 'registrations/signup_customer.html', {'user_form': user_form, 'customer_form': customer_form})

def login_customer(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and hasattr(user, 'customer'):
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'registrations/login_customer.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'registrations/login_customer.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login_customer')  

@login_required
def profile_overview(request):
    user = request.user
    return render(request, 'profilemanagement/profile_overview.html', {'user': user})

@login_required
def my_wallet(request):
    wallet = get_object_or_404(Wallet, user=request.user)
    return render(request, 'profilemanagement/my_wallet.html', {'wallet': wallet})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'profilemanagement/my_orders.html', {'orders': orders})


@login_required
def add_to_cart(request, item_id, model_name):
    # Get the content type for the given model_name
    model_class = {
        'trekkinggear': TrekkingGear,
        'camera': Camera,
        'ridinggear': RidingGear,
        'actioncamera': ActionCamera,
        'gamingconsole': GamingConsole,
        'winterwear': WinterWear,
        'audiovisualequipment': AudioVisualEquipment,
        'campinggear': CampingGear,
        'creatorgear': CreatorGear,
    }.get(model_name)

    if not model_class:
        return redirect('error_page')  # Handle the error case

    item = get_object_or_404(model_class, pk=item_id)
    content_type = ContentType.objects.get_for_model(item)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=item.id,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart')  # Redirect to the cart page
@login_required
def rent_from_cart(request, cart_item_id):
    # Get the specific cart item
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)

    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            
            # Create an order for the cart item
            order=Order.objects.create(
                user=request.user,
                content_type=cart_item.content_type,
                object_id=cart_item.object_id,
                quantity=cart_item.quantity,
                start_date=start_date,
                end_date=end_date,
                total_price=cart_item.total_price
            )
            
            # Remove the cart item after processing
            cart_item.delete()
            
            # Redirect to a confirmation page
            return redirect('order_confirmation', order_id=order.id)  # Adjust this if needed
    else:
        form = RentalForm()
    
    return render(request, 'profilemanagement/rent_from_cart.html', {'cart_item': cart_item, 'form': form})


@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'profilemanagement/cart.html', {'cart_items': cart_items})


@login_required
def delete_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')

@login_required
def increment_cart_item_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

@login_required
def decrement_cart_item_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()  # Remove item if quantity is 1
    return redirect('cart')


@login_required
def rent_item(request, item_id, model_name):
    # Get the content type for the given model_name
    model_class = {
        'trekkinggear': TrekkingGear,
        'camera': Camera,
        'ridinggear': RidingGear,
        'actioncamera': ActionCamera,
        'gamingconsole': GamingConsole,
        'winterwear': WinterWear,
        'audiovisualequipment': AudioVisualEquipment,
        'campinggear': CampingGear,
        'creatorgear': CreatorGear,
       

    }.get(model_name)

    if not model_class:
        return redirect('error_page')  # Handle the error case

    item = get_object_or_404(model_class, pk=item_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            
            # Create an order
            order = Order(
                user=request.user,
                content_type=ContentType.objects.get_for_model(item),
                object_id=item.id,
                quantity=quantity,
                start_date=start_date,
                end_date=end_date,
                order_date=timezone.now()
            )
            order.save()
            
            return redirect('order_confirmation', order_id=order.id)  # Redirect to a confirmation page or similar
    else:
        form = OrderForm()
    
    return render(request, 'profilemanagement/rent_item.html', {'item': item, 'form': form})
# views.py
@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'profilemanagement/order_confirmation.html', {'order': order})

@login_required
def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'profilemanagement/order_details.html', {'order': order})