from django.urls import path
from userauths import views
from . import views

app_name = "userauths"

urlpatterns = [
    path("sign-up/", views.register_view, name="register"),  # Ensure this name matches the one in your template
    path("sign-in/", views.login_view, name="sign-in"),
    path("logout/", views.logout_view, name="logout"),
]
