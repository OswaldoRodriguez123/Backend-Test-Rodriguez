from django.shortcuts import render, redirect
from menu.models import Order, Option
from django.core.exceptions import ValidationError
from django.contrib import messages
from cornershop.decorators import staff_member_required
import datetime

@staff_member_required(login_url='/login')
def home(request):
    orders = Order.objects.all()
    return render(request, 'order_home.html', {'orders': orders})

@staff_member_required(login_url='/login')
def edit(request, id):
    if request.method == 'GET':
        order = Order.objects.get(id=id)
        option = Option.objects.get(id=order.option_id)
        options = Option.objects.filter(menu_id=option.menu_id)
        
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        limit = '11:00:00'
        can_order = current_time <= limit
    
        data = {
            'action': '/order/edit/'+str(id)+'/',
            'id': order.id,
            'option_id': order.option_id,
            'employee_document': order.employee_document,
            'employee_name': order.employee_name,
            'details': order.details
        }
        return render(request, 'order_fields.html', {'data': data, 'options': options, 'can_order': can_order})
    else:
        order = Order.objects.get(id=id)
        order.option_id = request.POST['option_id']
        order.details = request.POST['details']
        order.employee_document = request.POST['employee_document']
        order.details = request.POST['details']
        try:
            order.full_clean()
            order.save()
            messages.success(request, 'Order was updated successfully!')
            return redirect('/orders')
        except ValidationError as e:
            messages.error(request, e)
            return redirect('/order/edit/'+str(id)+'/')

@staff_member_required(login_url='/login')
def delete(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    messages.error(request, 'Order was deleted successfully!')
    return redirect('/orders')

@staff_member_required(login_url='/login')
def view(request, id):
    order = Order.objects.get(id=id)
    order.viewed = True
    try:
        order.full_clean()
        order.save()
        messages.success(request, 'Order was viewed successfully!')
    except ValidationError as e:
        messages.error(request, e)
    return redirect('/orders')