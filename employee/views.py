from django.shortcuts import render, redirect
from django.views import View

from .models import Employee 
from .forms import EmployeeForm,UpdateEmployeeForm



class EmployeeView(View):
    def get(self, request,pk=None):

        if pk:
            obj = Employee.objects.get(id=pk)
            return render(request,'employee/detail.html',{'obj':obj})
        
        obj = Employee.objects.all()
        form = EmployeeForm()
        return render(request,'employee/dashboard.html',{'object':obj})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'employee/add_employee.html', {'form':form})


    form = EmployeeForm()
    return render(request,'employee/add_employee.html',{'form':form})


def update_employee(request,pk):
    obj = Employee.objects.get(id=pk)
    form = UpdateEmployeeForm(instance=obj)

    if request.method == 'POST':
        form = UpdateEmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request,'employee/update.html',{'form':form})

def delete_employee(request,pk):
    obj = Employee.objects.get(id=pk)
    obj.delete()
    return redirect('home') 
