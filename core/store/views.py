from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import DetailView
from . models import Product, Halaman, Contact, Visitor
from datetime import date, datetime
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.utils.translation import gettext, get_language, activate

import json




# Create your views here.
class HomeView(ListView):
    model = Product
    paginate_by = 10
    template_name = 'store/store.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        query = Halaman.objects.latest('updated_at')
        context['toko'] = query.nama_web
        context['about'] = gettext(query.tentang_toko)
        context['favicon'] = query.logo
        context['title'] = gettext('Store')
        

        return context
    
def loadmore(request, page):
    product = Product.objects.all().order_by('created_at')
    pagi = Paginator(product, 10)
    p = pagi.page(page)
    if p.has_next():
        next_page = p.next_page_number()
    else:
        next_page = 'last page'
    data = {}
    for obj in p:
        if obj.gambar:
            gambar = obj.gambar
        else:
            gambar = ''
        data[obj.nama] ={
            'nama':obj.nama, 
            'gambar':gambar, 
            'harga':obj.harga, 
            'slug': obj.slug, 
            } 
    return JsonResponse({'success':data, 'next': next_page})

# class DetailProduct(DetailView):
#     model = Product
#     template_name = 'store/detail.html'

#     def get_queryset(self):
#         self.slug = get_object_or_404(Product, slug=self.kwargs['slug'])
#         return Product.objects.get(slug=self.slug)
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         self.slug = self.kwargs['slug']
#         context['product'] = Product.objects.get(slug=str(self.slug))

def DetailProduct(request, slug):
    query = Product.objects.get(slug = slug)
    toko = Halaman.objects.latest('updated_at')
    context = {
        'product':query, 
        'toko': gettext(toko.nama_web), 
        'favicon':toko.logo,  
        'title': query.nama,
        'about': gettext(toko.tentang_toko),
        'instagram': toko.instagram,
        'facebook': toko.facebook,
        'phone': toko.phone,
        'wa_message': gettext(toko.wa_message),
    }
    return render(request, 'store/detail.html', context)

def add_contact(request):
    try:
        today = Contact.objects.get(created_at=date.today())
        if today:
            today.count += 1
            today.save()
            return JsonResponse({"success": today.count})
    except:
        new_contact = Contact.objects.create(count=1)
        
        return JsonResponse({"new": new_contact.count})


def add_visitor(request):
    try:
        today = Visitor.objects.get(created_at=date.today())
        if today:
            today.count += 1
            today.save()
            return JsonResponse({"visitor": today.count})
    except:
        new_visitor = Visitor.objects.create(count=1)
        return JsonResponse({"visitor": new_visitor.count})
    
def product_visitor(request, slug):
    product = Product.objects.get(slug=slug)
    if product:
        product.visitor_product = product.visitor_product + 1
        product.save()
        return JsonResponse({"success" : "visitor successfully added"})
    else:
        return JsonResponse({"visitor": 'Product not found'})
    
