from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['photo', 'name', 'birth_date', 'phone_number', 'email', 'address', 'subject', 'message']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
