from django.urls import path

from . import views
from .views import AdminProductsView

urlpatterns = [
    path('adminpanel', views.AdminView, name='admin-panel'),
    path('login', views.LoginView, name='login'),
    # path('admin-products', views.AdminProductsView, name='admin-products'),
    # path('findproduct', views.FindProduct, name='find'),
    path('findproduct', views.FindProduct, name='search'),
    path('products', AdminProductsView.as_view(), name='admin-products'),
    path('page', views.AdminPage, name='admin-page'),
    path('tokoinfo', views.TokoInfo, name='tokoinfo'),
    path('whatsapp', views.WhatsApp, name='whatsapp'),
    path('delete/<product_id>', views.delete_product, name='delete_product'),
    path('edit/<product_id>', views.edit_product, name='edit_product'),
    path('add-product', views.add_product, name='add_product'),
    path('profile/<profile_id>', views.delete_profile, name='delete_profile'),
]