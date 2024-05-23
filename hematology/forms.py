from django import forms
from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('patient_firstname', 'patient_lastname', 'patient_patronymic', 'patient_age', 'title', 'text')
    
