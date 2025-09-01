from .models import Polo
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def searchProducts(request):
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    polo = Polo.objects.distinct().filter(Q(name__icontains=search_query) |
                               Q(polo_sleeve__icontains=search_query) |
                               Q(polo_fit__icontains=search_query) |
                               Q(fabric__icontains=search_query) |
                               Q(tshirt_type__icontains=search_query) |
                               Q(ideal_for__icontains=search_query)
                               )
    return search_query, polo

def paginationPolo(request, polo, results):
    page = request.GET.get('page', 1)
    results = results
    paginator = Paginator(polo, results)
    
    try:
        polo = paginator.page(page)
    except PageNotAnInteger:
        polo = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        polo = paginator.page(page)
        
    leftIndex = (int(page) - 2)
    
    if leftIndex < 1:
        leftIndex = 1
        
    rightIndex = leftIndex + 5
    
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
        
    custom_range = range(leftIndex, rightIndex)
    return custom_range, polo
    
def paginationRound(request, roundNeck, results):
    page = request.GET.get('page', 1)
    results = results
    paginator = Paginator(roundNeck, results)
    
    try:
        roundNeck = paginator.page(page)
    except PageNotAnInteger:
        roundNeck = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        roundNeck = paginator.page(page)
        
    leftIndex = (int(page) - 2)
    
    if leftIndex < 1:
        leftIndex = 1
        
    rightIndex = leftIndex + 5
    
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
        
    custom_range = range(leftIndex, rightIndex)
    return custom_range, roundNeck
    
    
def paginationSearch(request, polo, results):
    page = request.GET.get('page', 1)
    results = results
    paginator = Paginator(polo, results)
    
    try:
        polo = paginator.page(page)
    except PageNotAnInteger:
        polo = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        polo = paginator.page(page)
        
    leftIndex = (int(page) - 2)
    
    if leftIndex < 1:
        leftIndex = 1
        
    rightIndex = leftIndex + 5
    
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
        
    custom_range = range(leftIndex, rightIndex)
    return custom_range, polo