from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Celestial
from django.core.paginator import Paginator
from cart.forms import CartAddCelestialForm

# Create your views here.

def index(request):
    celestial_objs = Celestial.objects.filter(available=True)
    return render(request, 'main/index.html', context={'celestial_objs': celestial_objs})

def category_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    celestial_objs = Celestial.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        celestial_objs = Celestial.objects.filter(category=category)
    paginator = Paginator(celestial_objs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/category_list.html', context={'category': category,
                                                               'celestial_objs': celestial_objs,
                                                               'categories': categories,
                                                               'page_obj': page_obj})

def detail(request, detail_slug):
    celestial_obj = get_object_or_404(Celestial, slug=detail_slug)
    cart_celestial_form = CartAddCelestialForm
    return render(request, 'main/detail.html', context={'celestial_obj': celestial_obj,
                                                        'cart_celestial_form': cart_celestial_form})
