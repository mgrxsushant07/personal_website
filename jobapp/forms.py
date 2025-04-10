from django import forms
from .models import candidate

class candidateForm(forms.ModelForm):
    class Meta:
        model = candidate
        fields = ['Full_Name', 'Date_of_Birth', 'CV', 'Cover_Letter', 'Remark']