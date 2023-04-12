from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from store.models import Product, Contact, Halaman
from django.http import JsonResponse
from django.views.generic import ListView
from datetime import date
from django.db.models import Sum
from django.core.paginator import Paginator


# Create your views here.
# def FindProduct(request):
#     product = Product.objects.all()
#     post = {}
#     for p in product:
#         post[p.nama]= {}
#         post[p.nama]['id'] = p.id
#         post[p.nama]['gambar'] = p.gambar.url 
#         post[p.nama]['deskripsi'] = p.deskripsi
#         post[p.nama]['harga'] = p.harga 
#     return JsonResponse(post)

def FindProduct(request):
    if request.user.is_authenticated:
    # post = {}
        if request.GET.get('table-search') is None:
            return redirect('admin-products')
        try:
            product = Product.objects.filter(nama__icontains=request.GET.get('table-search')).order_by('updated_at', 'created_at')
            page_obj = Paginator(product, 10)
            # if request.GET.get('page'):
            #     p = page_obj.page(request.GET.get('page'))
            # else:
            #     p = page_obj.page(1)
        except:
            product = Product.objects.all().order_by('updated_at')
            page_obj = Paginator(product, 10)
        if request.GET.get('page'):
            p = page_obj.page(request.GET.get('page'))
        else:
            p = page_obj.page(1)

        return render(request, 'members/admin-products.html',{'data':p, 'search':True, 'dataSearch':request.GET.get('table-search')})
    else:
        messages.warning(request,'You are not authenticated')
        return redirect('login')

def AdminPage(request):
    if request.user.is_authenticated:
        user = CurrentUser(request.user)
        try: 
            toko = Halaman.objects.latest('updated_at')
            # print(toko.nama_web)
            if toko.logo:
                return render(request, 'members/admin-pages.html',{'username': user['username'],'email': user['email'],'toko': toko, 'title': 'Pengaturan Toko', 'favicon':toko.logo, 'logo':toko.logo})
            return render(request, 'members/admin-pages.html',{'username': user['username'],'email': user['email'],'toko': toko, 'title': 'Pengaturan Toko'})

        except:
            return render(request, 'members/admin-pages.html',{'username': user['username'],'email': user['email'], 'title': 'Pengaturan Toko'})

    else:
        messages.error(request, 'You must login first')
        return redirect('/members/login')

def AdminView(request):
    if request.user.is_authenticated:
        today = date.today()
        product_now = Product.objects.filter(created_at__month=today.month).count()
        product_before = Product.objects.filter(created_at__month=today.month-1).count()

        product = Product.objects.order_by('-created_at')[:10]
        total_products = Product.objects.all().count()
        
        if (product_before == 0 and product_now == 0) or (product_before == 0 and product_now > 0) or (product_before == product_now):
            percentage_products = 0
            product_status = 'stag'
        elif product_before != 0 and (product_before > product_now):
            minus = product_before - product_now
            percentage_products = (minus/product_before)*100
            product_status = 'minus'
        else:
            plus = product_now - product_before
            percentage_products = (plus/product_before)*100
            product_status = 'plus'
        
        user = CurrentUser(request.user)
   
        contact_now = Contact.objects.filter(created_at__month=today.month).aggregate(bulan_ini=Sum('count'))
        contact_before = Contact.objects.filter(created_at__month__lt=today.month-1).aggregate(bulan_lalu=Sum('count'))
        total_contact = Contact.objects.all().aggregate(total=Sum('count'))
        
        if (contact_before['bulan_lalu'] == None and contact_now['bulan_ini'] == None) or (contact_before['bulan_lalu'] == None and contact_now['bulan_ini'] > 0) or (contact_before['bulan_lalu'] == contact_now['bulan_ini']):
            percentage_contact = 0
            contact_status = 'stag'
        elif contact_before['bulan_lalu'] != None and (contact_before['bulan_lalu']  > contact_now['bulan_ini']):
            minus = contact_before['bulan_lalu']  - contact_now['bulan_ini']
            percentage_contact = (minus/contact_before['bulan_lalu'] )*100
            contact_status = 'minus'
        else:
            plus = contact_now['bulan_ini'] - contact_before['bulan_lalu']  
            percentage_contact = (plus/contact_before['bulan_lalu'] )*100
            contact_status = 'plus'
        try:
            toko = Halaman.objects.latest('updated_at')
            phone = toko.phone
            favicon = toko.logo
        except:
            phone = 'Data telepon tidak ada'
            favicon = ''
        
        
        
        context = {
            'title': 'Admin Panel',
            'product': product, 
            'percentage_products': percentage_products,
            'total_products': total_products,
            'product_status': product_status,
            'username': user['username'],
            'email': user['email'],
            'total_contact': total_contact['total'],
            'percent_contact': percentage_contact,
            'contact_status': contact_status,
            'whatsapp': phone,
            'favicon': favicon
        }
        return render(request, 'members/admin-panel.html', context)
    else:
        messages.error(request, 'You must login first')
        return redirect('/members/login')
    
def CurrentUser(user):
    user = User.objects.get(username=user)
    return {'username':user.username, 'email':user.email}


class AdminProductsView(ListView):
    paginate_by=10
    model = Product
    template_name = 'members/admin-products.html'
    ordering = ('updated_at', 'created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = CurrentUser(self.request.user)
        halaman = Halaman.objects.latest('updated_at')
        context["username"] = user['username']
        context["email"] = user['email']
        context['title'] = 'Halaman Produk (Admin)'
        context['favicon'] = halaman.logo
        return context
    
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, 'You must login first')
            return redirect('/members/login')
        return super(AdminProductsView, self).get(*args, **kwargs)
    

def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth = authenticate(request, username=username, password=password)
    
        if auth is not None:
            login(request, auth)

            return redirect('admin-panel')
        else:
            return redirect('login')
    else:
        return render(request, 'members/login.html',{'title': 'Login'})
    
def TokoInfo(request):
    if request.method == 'POST' and request.user.is_authenticated:
        # print(request.POST)
        try:
            current_toko = Halaman.objects.get(id=request.POST.get('id'))
            # print(current_toko.nama_web, current_toko.updated_at)
            current_toko.nama_web = request.POST.get('nama-toko')
            current_toko.tentang_toko=request.POST.get('about')
            current_toko.email=request.POST.get('email')
            current_toko.country=request.POST.get('country')
            current_toko.city=request.POST.get('city')
            current_toko.address=request.POST.get('address')
            current_toko.phone=request.POST.get('phone-number')
            current_toko.zip = request.POST.get('zip-code')
            current_toko.instagram=request.POST.get('instagram') 
            current_toko.facebook=request.POST.get('facebook')
            current_toko.wa_message=request.POST.get('msg')
            try:
                if request.FILES['profile'] or request.POST.get('profile'):
                    if current_toko.logo:
                        current_toko.logo.delete()
                    current_toko.logo = request.FILES['profile'] 
                    print('profile updated successfully')
            except:
                pass
            # print(current_toko.instagram)
            messages.success(request,'Data saved successfully')
            current_toko.save()
        except:
            # print('data tidak ditemukan')
            create = Halaman.objects.create(nama_web=request.POST.get('nama-toko'),
                                                    logo = request.FILES['profile'],
                                                    tentang_toko=request.POST.get('about'),
                                                    email=request.POST.get('email'),
                                                    country=request.POST.get('country'),
                                                    city=request.POST.get('city'),
                                                    address=request.POST.get('address'),
                                                    phone=request.POST.get('phone-number'),
                                                    zip = request.POST.get('zip-code'),
                                                    instagram=request.POST.get('instagram'),
                                                    facebook=request.POST.get('facebook'),
                                                    wa_message=request.POST.get('msg'))
            create.save()
            messages.success(request,'Data created successfully')
        
        return redirect('admin-page')

def delete_profile(request, profile_id):
    if request.user.is_authenticated:
        profile = Halaman.objects.get(id=profile_id)
        profile.logo.delete()
        messages.success(request,'Logo deleted successfully')
        return redirect('admin-page')
    else:
        messages.warning(request,'You are not authenticated')
        return redirect('login')
    

def WhatsApp(request):
    if request.method=='POST' and request.user.is_authenticated:
        lastest = Halaman.objects.latest('updated_at')
        update = Halaman.objects.get(updated_at=lastest.updated_at)
        update.phone = request.POST.get('phone-number')
        update.save()
        messages.success(request,'Data saved successfully')
    
    return redirect('admin-panel')

def delete_product(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        product.gambar.delete()
        product.delete()
        messages.success(request,'Data deleted successfully')
        return redirect('admin-products')
    else:
        messages.warning(request, 'You do not have permission to delete this product')
        return redirect('login')

def edit_product(request, product_id):
    if request.user.is_authenticated:
        if request.method =='POST':
            product = Product.objects.get(id=product_id)
            if product:
                if request.POST.get('file_input'):
                    product.gambar.delete()
                    product.gambar = request.FILES['file_input']
                else:
                    pass
                product.nama = request.POST.get('nama')
                product.deskripsi = request.POST.get('deskripsi')
                product.harga = request.POST.get('harga')
                product.key_words = request.POST.get('keywords')

                product.save()
                messages.success(request, 'Product saved successfully')
                return redirect('admin-products')
            else:
                messages.error(request, 'Product failed to be saved')
                return redirect('edit_product')

        if product_id:
            product = Product.objects.get(id=product_id)
            return render(request, 'members/add_or_edit.html', {'product': product})
        else:
            return render(request, 'members/add_or_edit.html', {})
        
    
def add_product(request):
    if request.user.is_authenticated and request.method == 'POST':
        print(request.POST.get('file_input'))
        if request.POST.get('file_input'):
        # if request.POST.get('file_input') is not None and request.FILES is not None:
            p = Product.objects.create(nama=request.POST.get('nama'),
                                        gambar=request.FILES['file_input'],
                                        deskripsi=request.POST.get('deskripsi'),
                                        harga=request.POST.get('harga'),
                                        key_words=request.POST.get('keywords')
                                        )
            p.save()
            messages.success(request, 'Product added successfully')
            return redirect('admin-products')
        else:
            p = Product.objects.create(nama=request.POST.get('nama'),                                        
                                        deskripsi=request.POST.get('deskripsi'),
                                        harga=request.POST.get('harga'),
                                        key_words=request.POST.get('keywords')
                                        )
            p.save()
            messages.success(request, 'Product added successfully')
            return redirect('admin-products')
            
    return render(request, 'members/add_or_edit.html', {})

