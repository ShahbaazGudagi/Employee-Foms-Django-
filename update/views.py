from django.shortcuts import  redirect, render
from .models import *
from .forms import *
# Create your views here.

def AddEmployeeView(request):
    obj=AddEmployee.objects.all()
    return render(request,'view.html',{'obj':obj})


def Uploadform(request):
    form=EmployeeForms()
    if request.method=='POST':
        print('Print ',request.POST)
        form=EmployeeForms(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('/view/')
        else:
            print(form.errors)
    context={'form':form}
    return render(request, "form.html", context)


def RetriveForm(request,id):
    obj=AddEmployee.objects.get(id=id)
    return render(request,'single_view.html',{'obj':obj})
