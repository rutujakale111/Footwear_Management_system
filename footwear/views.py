from django.shortcuts import render, redirect
from .models import Footwear, Order

def footwear_list(request):
    products = Footwear.objects.all()
    return render(request, 'footwear/footwear_list.html', {'products': products})

def place_order(request, footwear_id):
    footwear = Footwear.objects.get(id=footwear_id)
    
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        total_price = footwear.price * quantity
        order = Order.objects.create(footwear=footwear, quantity=quantity, total_price=total_price)
        return redirect('order_success', order_id=order.id)
    
    return render(request, 'footwear/place_order.html', {'footwear': footwear})

def order_success(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'footwear/order_success.html', {'order': order})