from django.urls import path, include
from core.views import index, shop, about, blog, contact, cart, add_to_cart, remove_from_cart, login_view, register_view, logout_view, profile, checkout, payment_completed_view, payment_failed_view
from django.contrib.auth import views as auth_views

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("shop/", shop, name="shop"),
    path("about/", about, name="about"),
    path("blog/", blog, name="blog"),
    path("contact/", contact, name="contact"),
    path("cart/", cart, name="cart"),
    
    path("add-to-cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path('remove-from-cart/<int:item_id>/',remove_from_cart, name='remove_from_cart'),

    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    
    
    
    path('logout/', auth_views.LogoutView.as_view(next_page='core:index'), name='logout'),
    
    path('checkout/', checkout, name='checkout'),
    
    #path('accounts/', include('django.contrib.auth.urls')),
    
    
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment-completed/', payment_completed_view, name='payment-completed'),
    path('payment-failed/', payment_failed_view, name='payment-failed'),
]
