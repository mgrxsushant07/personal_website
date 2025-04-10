from django.shortcuts import render
from .forms import StudentForm
from django.http import HttpResponse
# Create your views here.


def student_registration(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'schoolapp/success.html')
    else:
        form = StudentForm()
    return render(request, 'schoolapp/student_registration.html', {'form': form})
