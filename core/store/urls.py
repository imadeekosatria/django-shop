from django.urls import path
from . import views

from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='store'),
    path('contact', views.add_contact, name='contact'),
    path('detail/<slug:slug>', views.DetailProduct, name='detail-product'),
    # path('visitor', views.add_visitor, name='visitor'),
    path('visitor/<slug:slug>', views.product_visitor, name='product-visitor'),
    path('<page>', views.loadmore, name='loadmore'),
]
