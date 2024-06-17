from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from django.shortcuts import  render
from django.contrib.auth.hashers import make_password
# from .models import Card
from django.http import HttpResponse
# Create your views here.
from cards.models import GPUs,Store,users_info

def Homepage(request):
    
    return render(request, 'Homepage.html')



def customer_login(request):
    print('wdwdwdww')
    if request.method == 'POST':
        email = request.POST['login']
        password = request.POST['passwd']
        
        try:
            user = users_info.objects.get(email=email)
            print(user, password, check_password(password, user.password))
            if check_password(password, user.password):
                # การตรวจสอบรหัสผ่านถูกต้อง
                return redirect('index')  # เปลี่ยนเส้นทางไปยังหน้า index
            else:
                # รหัสผ่านไม่ถูกต้อง
                return render(request, 'customer_login.html', {'error': 'Password is incorrect'})
        except users_info.DoesNotExist:
            # ไม่พบผู้ใช้ในระบบ
            return render(request, 'customer_login.html', {'error': 'User not found'})
    return render(request, 'customer_login.html')

def admin_login(request):
    
    return render(request, 'admin_login.html')


def forms(request):
    
    return render(request, 'forms.html')

def index(request):
    GPU_list = GPUs.objects.all
    return render(request, 'index.html',{'GPU_list':GPU_list})


def Customer(request):
    
    user_list = users_info.objects.all
    return render(request, 'user_manage.html',{'user_list':user_list})





def user_manage(request):
    user_list = users_info.objects.all()
    return render(request, 'user_manage.html', {'user_list': user_list})


def search_user(request):
    if request.method == 'POST':
        email = request.POST.get('search_email')
        try:
            user_list = users_info.objects.get(email=email)
            return render(request, 'user_manage.html', {'user_list': user_list})
        except users_info.DoesNotExist:
            return render(request, 'user_manage.html', {'error': 'User not found'})
    return redirect('user_manage')

def edit_user(request, user_id):
    if request.method == 'POST':
        user_list = get_object_or_404(users_info, id=user_id)
        user_list.name = request.POST.get('name')
        user_list.lastname = request.POST.get('lastname')
        user_list.email = request.POST.get('email')
        user_list.display_name = request.POST.get('display_name')
        user_list.phone_number = request.POST.get('phone_number')
        user_list.location = request.POST.get('location')
        user_list.birth_date = request.POST.get('birth_date')
        
        
        password = request.POST.get('password')
        if password:
            user_list.password = make_password(password)
        
        user_list.save()
        return redirect('user_manage')
    return redirect('user_manage')

def delete_user(request, user_id):
    user_list = get_object_or_404(users_info, id=user_id)
    user_list.delete()
    return redirect('user_manage')




































def store(request):
    stores = Store.objects.all()
    store_gpu_data = []

    for store in stores:
        try:
            gpu = GPUs.objects.get(products_id=store.graphics_card_id)
            store_gpu_data.append({
                'store_name': store.store_name,
                'store_num': store.store_num,

                'graphics_card_id': store.graphics_card_id,
                'brand': gpu.brand,
                'model': gpu.model
            })
        except GPUs.DoesNotExist:
            store_gpu_data.append({
                'store_name': store.store_name,
                'store_num': store.store_num,
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