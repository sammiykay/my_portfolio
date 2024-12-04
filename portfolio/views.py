from django.shortcuts import render
from .models import *
from django.http import JsonResponse
# Create your views here.
from .email_ import *

def index(request):
    portfolio = Portfolio.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')

        try:
            Contact.objects.create(name=name,email=email,message=message)
            send_thank_you_email(name, email, message)
            return JsonResponse({'message': 'Contact Submitted'})
        
        except Exception as e:
            return JsonResponse({'message': f'{e}'})

    context = {
        'portfolio': portfolio
    }
    return render(request,'index.html', context)