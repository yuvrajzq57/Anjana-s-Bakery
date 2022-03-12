from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from yuvraj.models import About

# Create your views here.
def yuvraj(request):
    return render(request, 'home.html')

def about(request):
   
    # We can handle the form here .
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Address = request.POST.get('Address')
        Landmark = request.POST.get('Landmark')
        City = request.POST.get('City')
        State = request.POST.get('State')
        Zip = request.POST.get('Zip')
        a = About(Name=(Name) , Address=(Address) , Landmark= (Landmark) ,City = (City) , State = (State) , Zip = (Zip) )
        a.save()
    else:
        pass
    return render(request, 'about.html')
     

def orders(request):
    return render(request, 'orders.html')

def cakes(request):
    return render(request, 'cakes.html')

def image(request):
    return render(request, 'image.html')


 