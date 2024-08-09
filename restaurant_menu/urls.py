from django.urls import path
from . import views

urlpatterns = [
    path("", views.MenuList.as_view(), name="home"),
    path("about/", views.AboutContent.as_view(), name="about"),
    path("detail/<int:pk>/", views.MenuItemDetail.as_view(), name="item_detail")

]