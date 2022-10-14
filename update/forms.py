from django.forms import ModelForm
from .models import *

class EmployeeForms(ModelForm):
    class Meta:
        model=AddEmployee
        fields='__all__'
