from django.shortcuts import render, redirect
from menu.models import Food
from django.core.exceptions import ValidationError
from django.contrib import messages
from cornershop.decorators import staff_member_required

@staff_member_required(login_url='/login')
def home(request):
    foods = Food.objects.all();
    return render(request, 'food_home.html', {'foods': foods})

@staff_member_required(login_url='/login')
def add(request):
    if request.method == 'GET':
        data = {
            'action': '/food/add/',
            'id': 0,
            'name': ''
        }
        return render(request, 'food_fields.html', {'data': data})
    else:
        food = Food(name=request.POST['name'])
        try:
            food.full_clean()
            food.save()
            messages.success(request, 'Food was created successfully!')
            return redirect('/food');
        except ValidationError as e:
            messages.error(request, e)
            return redirect('/food/add/');
    
@staff_member_required(login_url='/login')
def edit(request, id):
    if request.method == 'GET':
        food = Food.objects.get(id=id)
        data = {
            'action': '/food/edit/'+str(id)+'/',
            'id': food.id,
            'name': food.name
        }
        return render(request, 'food_fields.html', {'data': data})
    else:
        food = Food.objects.get(id=id)
        food.name = request.POST['name']
        try:
            food.full_clean()
            food.save()
            messages.success(request, 'Food was updated successfully!')
            return redirect('/food')
        except ValidationError as e:
            messages.error(request, e)
            return redirect('/food/edit/'+str(id)+'/')

@staff_member_required(login_url='/login')
def delete(request, id):
    food = Food.objects.get(id=id)
    food.delete()
    messages.error(request, 'Food was deleted successfully!')
    return redirect('/food')