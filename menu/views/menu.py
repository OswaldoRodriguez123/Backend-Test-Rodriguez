from django.shortcuts import render, redirect
from menu.models import Menu, Option, Order
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.utils import timezone, dateformat
from cornershop.decorators import staff_member_required
from menu.tasks import send_menu
import datetime

@staff_member_required(login_url='/login')
def home(request):
    menus = Menu.objects.all();
    return render(request, 'menu_home.html', {'menus': menus})

@staff_member_required(login_url='/login')
def add(request):
    if request.method == 'GET':
        data = {
            'action': '/menu/add/',
            'id': 0,
            'name': '',
            'date': dateformat.format(timezone.now(), 'Y-m-d')
        }
        return render(request, 'menu_fields.html', {'data': data})
    else:
        menu = Menu(name=request.POST['name'],date=request.POST['date'])
        try:
            menu.full_clean()
            menu.save()
            messages.success(request, 'Menu was created successfully!')
            return redirect('/menu')
        except ValidationError as e:
            messages.error(request, e)
            return redirect('/menu/add/')
    
@staff_member_required(login_url='/login')
def edit(request, id):
    if request.method == 'GET':
        menu = Menu.objects.get(id=id)
        data = {
            'action': '/menu/edit/'+str(id)+'/',
            'id': menu.id,
            'name': menu.name,
            'date': dateformat.format(menu.date, 'Y-m-d')
        }
        return render(request, 'menu_fields.html', {'data': data})
    else:
        menu = Menu.objects.get(id=id)
        menu.name = request.POST['name']
        menu.date = request.POST['date']
        try:
            menu.full_clean()
            menu.save()
            messages.success(request, 'Menu was updated successfully!')
            return redirect('/menu')
        except ValidationError as e:
            messages.error(request, e)
            return redirect('/menu/edit/'+str(id)+'/')

@staff_member_required(login_url='/login')
def delete(request, id):
    menu = Menu.objects.get(id=id)
    menu.delete()
    messages.error(request, 'Menu was deleted successfully!')
    return redirect('/menu')

def options(request, uuid):
    menu = Menu.objects.get(uuid=uuid)
    options = Option.objects.filter(menu_id=menu.id)

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    limit = '11:00:00'
    can_order = current_time <= limit
        
    if request.method == 'GET':
        data = {
            'action': uuid,
            'id': 0,
            'employee_document': '',
            'employee_name': '',
            'details': ''
        }
        return render(request, 'order_fields.html', {'data': data, 'options': options, 'can_order' : can_order})
    else:
        order = Order(
                    employee_document=request.POST['employee_document'],
                    employee_name=request.POST['employee_name'],
                    option_id=request.POST['option_id'],
                    details=request.POST['details']
                )
        try:
            order.full_clean()
            order.save()
            messages.success(request, 'Order was created successfully!')
        except ValidationError as e:
            messages.error(request, e)
        except Exception as e:
            messages.error(request, e)
        return redirect('/menu/'+str(uuid))

@staff_member_required(login_url='/login')
def send(request, id):
    menu_options = Option.objects.filter(menu_id=id)
    menu = Menu.objects.get(id=id)
    options = ""
    for i, option in enumerate(menu_options):
        options += 'Option ' + str(i+1)+': ' + str(option.food.name) + '\n'

    try:
        send_menu(options,menu.uuid)
        messages.success(request, 'Menu was sent successfully!')
    except ValidationError as e:
        messages.error(request, e)
    return redirect('/menu')