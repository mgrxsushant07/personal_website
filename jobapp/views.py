from django.shortcuts import render
from .forms import candidateForm
# Create your views here.

def candidate_registration(request):
    if request.method == 'POST':
        form = candidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'jobapp/success.html')
    else:
        form = candidateForm()
    return render(request, 'jobapp/job_registration.html', {'form': form})
