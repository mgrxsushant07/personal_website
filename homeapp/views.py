# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import contactform  

def index(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'homeapp/success.html')
    else:
        form = contactform()  

    return render(request, 'homeapp/index.html', {'form': form})  