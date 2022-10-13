from django.shortcuts import  render
from .models import *
from .forms import *

from django.urls import reverse
# Create your views here.

def AddEmployeeView(request):
    obj=AddEmployee.objects.all()
    return render(request,'view.html',{'obj':obj})


def Uploadform(request):
    form=EmployeeForms()
    if request.method=='POST':
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request, "form.html", context)

