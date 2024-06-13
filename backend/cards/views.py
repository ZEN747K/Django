from django.shortcuts import render, get_object_or_404
# from .models import Card
from django.http import HttpResponse
# Create your views here.
from cards.models import GPUs,Store

def Homepage(request):
    
    return render(request, 'Homepage.html')



def Customer_login(request):
    
    return render(request, 'Customer_login.html')

def admin_login(request):
    
    return render(request, 'admin_login.html')


def forms(request):
    
    return render(request, 'forms.html')

def index(request):
    GPU_list = GPUs.objects.all
    return render(request, 'index.html',{'GPU_list':GPU_list})


def Customer(request):
    
    return render(request, 'Customer.html')

def user_manage(request):
    
    return render(request, 'user_manage.html')

def store(request):
    stores = Store.objects.all()
    store_gpu_data = []

    for store in stores:
        try:
            gpu = GPUs.objects.get(products_id=store.graphics_card_id)
            store_gpu_data.append({
                'store_name': store.store_name,
                'graphics_card_id': store.graphics_card_id,
                'brand': gpu.brand,
                'model': gpu.model
            })
        except GPUs.DoesNotExist:
            store_gpu_data.append({
                'store_name': store.store_name,
                'graphics_card_id': store.graphics_card_id,
                'brand': 'N/A',
                'model': 'N/A'
            })
    
    return render(request, 'store.html', {'store_gpu_data': store_gpu_data})


# def card_list(request):
#     cards = Card.objects.all()
#     return render(request, 'cards/index.html', {'cards': cards})

# def card_detail(request, pk):
#     card = get_object_or_404(Card, pk=pk)
#     return render(request, 'cards/card_detail.html', {'card': card})