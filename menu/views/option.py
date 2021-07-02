from django.shortcuts import render, redirect
from menu.models import Option, Food
from django.core.exceptions import ValidationError
from django.contrib import messages
from cornershop.decorators import staff_member_required

@staff_member_required(login_url='/login')
def home(request, menu_id):
    options = Option.objects.filter(menu_id=menu_id);
    return render(request, 'option_home.html', {'menu_id': menu_id, 'options': options})

@staff_member_required(login_url='/login')
def add(request, menu_id):
    if request.method == 'GET':
        foods = Food.objects.all();
        data = {
            'action': '/menu/options/add/'+str(menu_id),
            'id': 0,
            'food_id': 0
        }
        return render(request, 'option_fields.html', {'menu_id': menu_id, 'foods': foods, 'data': data})
    else:
        option = Option(food_id=request.POST['food_id'],menu_id=menu_id)
        try:
            option.full_clean()
            option.save()
            messages.success(request, 'Option was created successfully!')
            return redirect('/menu/options/'+str(menu_id))
        except ValidationError as e:
            messages.error(request, e)
            return redirect('/menu/options/add/'+str(menu_id))
    
@staff_member_required(login_url='/login')
def edit(request, id):
    if request.method == 'GET':
        foods = Food.objects.all();
        option = Option.objects.get(id=id)
        data = {
            'action': '/menu/option/edit/'+str(id)+'/',
            'id': option.id,
            'food_id': option.food_id
        }
        return render(request, 'option_fields.html', {'menu_id': option.menu_id, 'foods': foods, 'data': data})
    else:
        option = Option.objects.get(id=id)
        option.food_id = request.POST['food_id']
        try:
            option.full_clean()
            option.save()
            messages.success(request, 'Option was updated successfully!')
            return redirect('/menu/options/'+str(option.menu_id))
        except ValidationError as e:
            messages.error(request, e)
            return redirect('/menu/option/edit/'+str(id)+'/')

@staff_member_required(login_url='/login')
def delete(request, id):
    option = Option.objects.get(id=id)
    option.delete()
    messages.error(request, 'Option was deleted successfully!')
    return redirect('/menu/options/'+str(option.menu_id))