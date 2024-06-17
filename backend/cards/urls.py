from django.urls import path
from . import views




urlpatterns = [
    path('list', views.index),
    path('', views.Homepage),
    path('user', views.customer_login,name='customer_login'),
    path('admin_login', views.admin_login),
    path('GPU', views.forms),
    path('Customer', views.Customer),
    
    path('user_manage/', views.user_manage, name='user_manage'),
    path('search_user/', views.search_user, name='search_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),

    






    path('stores', views.store),
    # path('GPU', views.card_list),
    
]


# urlpatterns = [
#     path('', views.card_list, name='card_list'),
#     path('<int:pk>/', views.card_detail, name='card_detail'),
# ]