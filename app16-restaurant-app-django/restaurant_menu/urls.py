from django.urls import path
from . import views

urlpatterns = [
    path('', views.Menulist.as_view(), name='home'),
    # /<int:pk>/: Jinja syntax to handle dynamic urls
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name='menu_item'),
]