from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Polo, PoloImage, Wishlist, Homepage
from .forms import TShirtForm, PoloImageForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import searchProducts, paginationSearch, paginationRound, paginationPolo

products_per_page = 6
def home(request):
    promotional = Homepage.objects.get(name='home-page')
    allProducts = Polo.objects.all()[:10]
    polo = Polo.objects.filter(tshirt_type='polo')[:10]
    roundNeck = Polo.objects.filter(tshirt_type='round')[:10]
    return render(request, 'index.html', {'polo': polo, 'round': roundNeck, 'all': allProducts, 'promo': promotional})

def polos(request):
    polo = Polo.objects.filter(tshirt_type='polo')
    custom_range, polo = paginationPolo(request, polo, products_per_page)
    return render(request, 'polos.html', {'polos': polo, 'custom_range': custom_range})

def roundNeck(request):
    roundNeck = Polo.objects.filter(tshirt_type='round')
    custom_range, roundNeck = paginationRound(request, roundNeck, products_per_page)
    return render(request, 'round.html', {'round': roundNeck, 'custom_range': custom_range})

def searchPage(request):
    search_query, polo = searchProducts(request)
    custom_range = paginationSearch(request, polo, products_per_page)
    return render(request, 'search.html', {'polos': polo, 'search_query': search_query, 'custom_range': custom_range})

def detail(request, id):
    polo_instance = get_object_or_404(Polo, pk=id)
    
    if request.method == 'POST':
        form = TShirtForm(request.POST, instance=polo_instance)
        image_form = PoloImageForm(request.POST, request.FILES)
        
        if form.is_valid() and image_form.is_valid():
            form.save()
            polo_image = PoloImage(image=image_form.cleaned_data['image'], polo=polo_instance)
            polo_image.save()
            return redirect('polos')
    
    else:
        form = TShirtForm(instance=polo_instance)
        image_form = PoloImageForm()
    
    return render(request, 'single-product.html', {'polo': polo_instance, 'form': form, 'image_form': image_form})


def privacyPolicy(request):
    return HttpResponse('Privacy policy is available')

def exchangeAndReturns(request):
    return render(request, 'return-exchange.html')


def policy(request):
    return render(request, 'policy.html')

def aboutUs(request):
    return render(request, 'about.html')

def shipping(request):
    return render(request, 'shipping.html')



def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # For example, you can send an email or save to the database
            # Here, we'll just redirect or render a success message
            form.save()
            return render(request, 'contact_success.html')  # Create this template for success message
    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {'form': form})

@login_required(login_url='login')
def createProduct(request):
    form = TShirtForm()
    
    if request.method == 'POST':
        form = TShirtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polos')
    
    context = {'form': form}
    return render(request, 'project_form.html', context)

def updateProduct(request, pk):
    product = Polo.objects.get(id=pk)
    form = TShirtForm(instance=product)
    
    if request.method == 'POST':
        form = TShirtForm(request.POST, instance = product)
        if form.is_valid():
            form.save()
            return redirect('polos')
    
    context = {'form': form}
    return render(request, 'project_form.html', context)

def deleteProduct(request, pk):
    product = Polo.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('polos')
    context = {'object': product}
    return render(request, 'delete_product.html', context)



@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Polo, id=product_id)
    # Create a new wishlist entry or do nothing if it already exists
    Wishlist.objects.get_or_create(user=request.user, product=product)
    messages.success(request, f'{product.name} has been added to your wishlist!')
    return redirect('wishlist')  # Redirect back to the product list or wherever you want


@login_required
def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})


def loginPage(request):
    return render(request, 'login.html')
