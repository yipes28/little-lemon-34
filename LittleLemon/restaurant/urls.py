from django.contrib import admin
from django.urls import path
from .views import index, MenuItemView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", index, name="home"),
    path("menu/", MenuItemView.as_view(), name="menuitem_list"),
    path("menu/<int:pk>", SingleMenuItemView.as_view(), name="single_menuitem"),
    path("api-token-auth", obtain_auth_token),
]
