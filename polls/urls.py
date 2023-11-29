from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("ministries/", views.MinistriesView.as_view(), name="ministries"),
    path("giving/", views.GivingView.as_view(), name="giving"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]