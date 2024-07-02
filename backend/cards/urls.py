from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('list', views.gpu_information, name='list'),
    path('', views.Homepage),
    path('store', views.store, name='store'),
    path('user', views.customer_login,name='customer_login'),
    path('logout', views.customer_logout, name='customer_logout'),
    path('admin_login', views.admin_login,name='admin_login'),
    path('admin_logout', views.admin_logout,name='admin_logout'),
    path('gpu_manage', views.gpu_manage,name='gpu_manage'),
    path('Customer', views.Customer,name='Customer'),
    
    path('user_manage/', views.user_manage, name='user_manage'),
    path('search_user/', views.search_user, name='search_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('store_manage/', views.store_manage, name='store_manage'),
    path('search_store/', views.store_manage, name='search_store'),
    path('add_store/', views.add_store, name='add_store'),
    path('edit_store/<int:store_id>/', views.edit_store, name='edit_store'),
    path('delete_store/<int:id>/', views.store_manage, name='delete_store'),
    # path('GPU', views.card_list),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path('', views.card_list, name='card_list'),
#     path('<int:pk>/', views.card_detail, name='card_detail'),
# ]