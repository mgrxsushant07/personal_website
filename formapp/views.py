from django.shortcuts import render
from .forms import FeedbackForm

def feedback(request):
    form = FeedbackForm()
    return render(request, 'formapp/feedback.html', {'form': form})