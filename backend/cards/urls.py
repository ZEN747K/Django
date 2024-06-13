from django.urls import path
from . import views




urlpatterns = [
    path('list', views.index),
    path('', views.Homepage),
    path('user', views.Customer_login),
    path('admin_login', views.admin_login),
    path('GPU', views.forms),
    path('Customer', views.Customer),
    path('user_manage', views.user_manage),
    path('store', views.store),
    # path('GPU', views.card_list),
    
]


# urlpatterns = [
#     path('', views.card_list, name='card_list'),
#     path('<int:pk>/', views.card_detail, name='card_detail'),
# ]