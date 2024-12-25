from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import *
from .models import *
from .forms import *


def index(request: WSGIRequest):
    flowers = Flowers.objects.filter(published=True)
    context = {
        'flowers': flowers
    }

    return render(request, 'index.html', context)


def category(request: WSGIRequest, type_id):
    type = get_object_or_404(Categories, id=type_id)
    flowers = Flowers.objects.filter(type_id=type_id, published=True)
    context = {
        'type': type,
        'flowers': flowers
    }

    return render(request, 'type_detail.html', context)


def flower(request: WSGIRequest, flower_id):
    flower = get_object_or_404(Flowers, id=flower_id, published=True)

    context = {
        'flower': flower
    }
    return render(request, 'detail.html', context)


def add_species(request: WSGIRequest):
    if request.method == 'POST':
        form = CategoriesForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            species = Categories.objects.create(**form.cleaned_data)
            return redirect('type_detail', type_id=species.id)
    form = CategoriesForm()
    context = {
        'form': form,
        'title': "O'simlik turi qo'shish"
    }
    return render(request, 'add_species.html', context)


def add_flowers(request: WSGIRequest):
    if request.method == 'POST':
        form = FlowerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            flowers = Flowers.objects.create(**form.cleaned_data)
            return redirect('flower_detail', flower_id=flowers.pk)

    form = FlowerForm()
    context = {
        'form': form,
        'title': "Gul qo'shish"
    }
    return render(request, 'add_flowers.html', context)


def update_species(request: WSGIRequest, type_id):
    species = get_object_or_404(Categories, id=type_id)

    if request.method == 'POST':
        form = CategoriesForm(data=request.POST)
        if form.is_valid():
            species.name = form.cleaned_data.get('name')
            species.definition = form.cleaned_data.get('definition')
            species.save()
            return redirect('type_detail', type_id=species.id)

    form = CategoriesForm(initial={
        'name': species.name,
        'definition': species.definition
    })

    context = {
        'form': form
    }

    return render(request, 'add_species.html', context)


def update_flowers(request: WSGIRequest, flower_id):
    flowers = get_object_or_404(Flowers, id=flower_id)
    if request.method == 'POST':
        form = CategoriesForm(data=request.POST)
        if form.is_valid():
            flowers.name = form.cleaned_data.get('name')
            flowers.price = form.cleaned_data.get('price')
            flowers.published = form.cleaned_data.get('published')
            flowers.type = form.cleaned_data.get('type')
            flowers.quantity = form.cleaned_data.get('quantity')
            flowers.description = form.cleaned_data.get('description')
            flowers.save()
            return redirect('flower_detail')
    form = FlowerForm(initial={
        'name': flowers.name,
        'description': flowers.description,
        'price': flowers.price,
        'published': flowers.published,
        'type': flowers.type,
        'quantity': flowers.quantity
    })
    context = {
        'form': form
    }
    return render(request, 'add_flowers.html', context)


def delete_type(request, type_id):
    type = get_object_or_404(Categories, id=type_id)

    if request.method == 'POST':
        type.delete()
        messages.success(request, "Tur muvaffaqiyatli tarzda o'chirildi!")
        return redirect('home')

    messages.warning(request, "Ushbu tur o'chirib tashlamoqchimisiz!")
    return render(request, 'confirm_delete.html', {'type': type})


def delete_flowers(request, flower_id):
    flower = get_object_or_404(Flowers, id=flower_id)

    if request.method == 'POST':
        flower.delete()
        messages.success(request, "Gul muvaffaqiyatli tarzda o'chirildi!")
        return redirect('home')

    messages.warning(request, "Ushbu gulni o'chirib tashlamoqchimisiz!")
    return render(request, 'confirm_delete_for_flowers.html', {'flower': flower})

