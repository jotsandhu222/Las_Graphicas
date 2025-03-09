from django.http import HttpResponse
from django.shortcuts import render
from .models import TShirt, Polo

def tshirts(request):
    data = TShirt.objects.all()
    return render(request, 'LasGraphicas.html', {'tshirts': data})

def home(request):
    data = Polo.objects.all()
    return render(request, 'index.html', {'polo': data})

def polos(request):
    data = Polo.objects.all()
    #return HttpResponse("Hello, world. You're at the polos home page.")
    return render(request, 'polos.html', {'polos': data})

def detail(request, id):
    data = Polo.objects.get(pk=id)
    return render(request, 'detail.html', {'polo': data})

def add(request):
    name = request.POST.get('name')
    price = request.POST.get('price')
    return render(request, 'add.html')


def privacyPolicy(request):
    return HttpResponse('Privacy policy is available')

def exchangeAndReturns(request):
    return HttpResponse('exchange and returns')


def cancellationPolicy(request):
    return HttpResponse('cancellation policy')


from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # For example, you can send an email or save to the database
            # Here, we'll just redirect or render a success message
            return render(request, 'contact_success.html')  # Create this template for success message
    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {'form': form})