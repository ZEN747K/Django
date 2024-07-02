from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from django.shortcuts import  render
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
# from .models import Card
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.
from cards.models import GPUs,Store,users_info,UserProfile  
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q

def Homepage(request):
    
    return render(request, 'Homepage.html')



def customer_login(request):
    if request.method == 'POST':
        email = request.POST.get('login')
        password = request.POST.get('passwd')
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                login(request, user)
                return redirect('customer_login')
            else:
                return render(request, 'customer_login.html', {'error': 'Invalid login credentials'})
        except User.DoesNotExist:
            return render(request, 'customer_login.html', {'error': 'Invalid login credentials'})
    return render(request, 'customer_login.html')

@login_required
def customer_logout(request):
    logout(request)
    return redirect('customer_login')


def store(request):
    store = Store.objects.all()
    return render(request, 'store.html', {'store': store})












    

def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('login')
        password = request.POST.get('passwd')
        
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('admin_login')
            else:
                messages.error(request, 'Invalid login credentials or you are not authorized to access this page.')
        except User.DoesNotExist:
            messages.error(request, 'Invalid login credentials or you are not authorized to access this page.')
            
    return render(request, 'admin_login.html')
@login_required
def admin_logout(request):
    logout(request)
    return redirect('admin_login')





@login_required
def gpu_manage(request):
    gpus = GPUs.objects.all()
    gpu = None
    last_modified_by_name = request.user.username
    
    if request.method == 'POST':
        if 'search' in request.POST:
            gpu_id = request.POST.get('gpu_id')
            gpu = get_object_or_404(GPUs, GPU_id=gpu_id)
        
        elif 'add_new' in request.POST:
            gpu = GPUs()
        
        elif 'save' in request.POST:
            gpu_id = request.POST.get('gpu_id')
            gpu, created = GPUs.objects.get_or_create(GPU_id=gpu_id)
            
            gpu.brand = request.POST.get('brand')
            gpu.model = request.POST.get('model')
            gpu.slot = request.POST.get('slot')
            gpu.chipset = request.POST.get('chipset')
            gpu.series = request.POST.get('series')
            gpu.gpu_model = request.POST.get('gpu_model')
            gpu.gpu_speed_oc = request.POST.get('gpu_speed_oc')
            gpu.gpu_speed_gaming = request.POST.get('gpu_speed_gaming')
            gpu.memory_speed = request.POST.get('memory_speed')
            gpu.memory_size = request.POST.get('memory_size')
            gpu.memory_type = request.POST.get('memory_type')
            gpu.cuda_cores = request.POST.get('cuda_cores')
            gpu.length = request.POST.get('length')
            gpu.width = request.POST.get('width')
            gpu.height = request.POST.get('height')
            gpu.max_resolution = request.POST.get('max_resolution')
            gpu.directx_support = request.POST.get('directx_support')
            gpu.crossfire_sli_support = request.POST.get('crossfire_sli_support')
            gpu.dvi_port = request.POST.get('dvi_port')
            gpu.hdmi_port = request.POST.get('hdmi_port')
            gpu.display_port = request.POST.get('display_port')
            gpu.option_port = request.POST.get('option_port')
            gpu.power_consumption = request.POST.get('power_consumption')
            gpu.power_supply_requirement = request.POST.get('power_supply_requirement')
            gpu.power_connectors = request.POST.get('power_connectors')
            gpu.warranty_years = request.POST.get('warranty_years')

            if 'image' in request.FILES:
                image = request.FILES['image']
                fs = FileSystemStorage(location=settings.MEDIA_ROOT + '/gpu_images')
                filename = fs.save(image.name, image)
                gpu.image = 'gpu_images/' + filename

            gpu.save()
        
        elif 'delete' in request.POST:
            gpu_id = request.POST.get('gpu_id')
            gpu = get_object_or_404(GPUs, GPU_id=gpu_id)
            gpu.delete()
            return redirect('gpu_manage')

        elif 'edit' in request.POST:
            gpu_id = request.POST.get('gpu_id')
            gpu = get_object_or_404(GPUs, GPU_id=gpu_id)
    
    return render(request, 'gpu_manage.html', {'gpus': gpus, 'gpu': gpu, 'last_modified_by_name': last_modified_by_name})













def gpu_information(request):
    if request.method == 'GET':
        gpu_id = request.GET.get('gpu_id')
        brand = request.GET.get('brand')
        chipset = request.GET.get('chipset')
        series = request.GET.get('series')
        max_resolution = request.GET.get('max_resolution')

        filters = Q()

        if gpu_id:
            filters &= Q(GPU_id__icontains=gpu_id)
        if brand:
            filters &= Q(brand__icontains=brand)
        if chipset:
            filters &= Q(chipset__icontains=chipset)
        if series:
            filters &= Q(series__icontains=series)
        if max_resolution:
            filters &= Q(max_resolution__icontains=max_resolution)

        GPU_list = GPUs.objects.filter(filters)
    else:
        GPU_list = GPUs.objects.all()

    return render(request, 'index.html', {'GPU_list': GPU_list})







def Customer(request):
    
    user_list = users_info.objects.all
    return render(request, 'Customer.html',{'user_list':user_list})




@login_required
def user_manage(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)
    return render(request, 'user_manage.html', {'user': user, 'profile': profile})

def search_user(request):
    if request.method == 'POST':
        email = request.POST.get('search_email')
        try:
            user = User.objects.get(email=email)
            profile, created = UserProfile.objects.get_or_create(user=user)
            return render(request, 'user_manage.html', {'user': user, 'profile': profile})
        except User.DoesNotExist:
            return render(request, 'user_manage.html', {'error': 'User not found'})
    return redirect('user_manage')

@login_required
def edit_user(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        profile = get_object_or_404(UserProfile, user=user)

        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')

        password = request.POST.get('password')
        if password:
            user.password = make_password(password)

        user.save()

        profile.last_modified_by = request.user
        profile.save()

        return redirect('user_manage')
    return redirect('user_manage')

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('user_manage')

@login_required
def edit_store(request, store_id):
    stores = Store.objects.all()
    store = get_object_or_404(Store, store_id=store_id)
    if request.method == 'POST':
        
        store.store_name = request.POST.get('store_name')
        store.store_num = int(request.POST.get('store_num'))
        store.graphics_card_id = request.POST.get('graphics_card_id')
        store.gpu = GPUs.objects.get(GPU_id=request.POST.get('graphics_card_id'))
        store.products = request.POST.get('products')
        store.last_modified_by = request.user
        store.save()
    return render(request, 'store_manage.html', {'store': store, 'stores': stores})

@login_required
def add_store(request):
    store = None
    error = None
    if request.method == 'POST':
        store_name = request.POST.get('store_name')
        store_num = request.POST.get('store_num')
        graphics_card_id = request.POST.get('graphics_card_id')
        products = request.POST.get('products')
        gpu = GPUs.objects.get(GPU_id=graphics_card_id)
        store = Store(store_name=store_name, store_num=store_num, graphics_card_id=graphics_card_id, products=products, gpu=gpu, last_modified_by=request.user)
        store.save()
    return render(request, 'store_manage.html', {'store': store, 'error': error})

@login_required
def store_manage(request):
    store = None
    error = None
    stores = Store.objects.all()  
    if request.method == 'POST':
        if 'search_name' in request.POST:
            search_name = request.POST.get('search_name')
            try:
                store = Store.objects.get(store_name=search_name)
                stores = [store]  
            except Store.DoesNotExist:
                error = 'Store not found.'
        elif 'edit' in request.POST:
            store_id = request.POST.get('store_id')
            store = get_object_or_404(Store, store_id=store_id)
    return render(request, 'store_manage.html', {'store': store, 'error': error, 'stores': stores})

# def card_list(request):
#     cards = Card.objects.all()
#     return render(request, 'cards/index.html', {'cards': cards})

# def card_detail(request, pk):
#     card = get_object_or_404(Card, pk=pk)
#     return render(request, 'cards/card_detail.html', {'card': card})