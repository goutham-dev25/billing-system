from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import MenuItem, Order, OrderItem
from django.db.models import Sum
from datetime import datetime

@login_required
def menu(request):
    items = MenuItem.objects.all()
    categories = ['Breakfast', 'Lunch', 'Dinner']
    cart = request.session.get('cart', {})
    cart_items = []
    cart_total = 0
    for item_id, qty in cart.items():
        item = MenuItem.objects.get(id=int(item_id))
        subtotal = item.price * qty
        cart_total += subtotal
        cart_items.append({'item': item, 'qty': qty, 'subtotal': subtotal})
    context = {
        'items': items,
        'categories': categories,
        'cart_items': cart_items,
        'cart_total': cart_total
    }
    return render(request, 'menu/menu.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            return render(request, 'menu/login.html', {'error': 'Invalid credentials'})
    return render(request, 'menu/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'menu/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    cart = request.session.get('cart', {})
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    request.session['cart'] = cart
    return JsonResponse({'success': True})

@login_required
def cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for item_id, qty in cart.items():
        item = MenuItem.objects.get(id=int(item_id))
        subtotal = item.price * qty
        total += subtotal
        items.append({'item': item, 'qty': qty, 'subtotal': subtotal})
    order = request.GET.get('order')
    if order:
        order_obj = Order.objects.get(id=order)
        return render(request, 'menu/cart.html', {'items': items, 'total': total, 'order': order_obj, 'upi_id': 'gouthammuthusamy2002-1@oksbi'})
    return render(request, 'menu/cart.html', {'items': items, 'total': total})

@login_required
def checkout(request):
    if request.method in ['POST', 'GET']:
        cart = request.session.get('cart', {})
        if not cart:
            return redirect('cart')
        order = Order.objects.create(total=0)
        total = 0
        for item_id, qty in cart.items():
            item = MenuItem.objects.get(id=int(item_id))
            OrderItem.objects.create(order=order, item=item, quantity=qty)
            total += item.price * qty
        order.total = total
        order.save()
        request.session['cart'] = {}
        return redirect(f'/cart/?order={order.id}')
    return redirect('cart')

@login_required
def get_cart_data(request):
    cart = request.session.get('cart', {})
    cart_items = []
    cart_total = 0
    for item_id, qty in cart.items():
        item = MenuItem.objects.get(id=int(item_id))
        subtotal = item.price * qty
        cart_total += subtotal
        cart_items.append({'name': item.name, 'qty': qty, 'subtotal': subtotal})
    return JsonResponse({'cart_items': cart_items, 'cart_total': cart_total})

@login_required
def clear_cart(request):
    request.session['cart'] = {}
    return redirect('cart')


@login_required
def sales_report(request):
    current_month = datetime.now().month
    current_year = datetime.now().year
    orders = Order.objects.filter(date__year=current_year, date__month=current_month)
    total_sales = orders.aggregate(Sum('total'))['total__sum'] or 0
    order_count = orders.count()
    return render(request, 'menu/sales_report.html', {'total_sales': total_sales, 'order_count': order_count})