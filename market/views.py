from django.shortcuts import render
from market.models import Prodyct, Employee

def prodyct(request):
    products = Prodyct.objects.all()
    context = {'product': products}
    return render(request, 'prodyct.html', context)


def employee(request):
    employes = Employee.objects.all()
    contex = {'employee': employee}
    return render(request, 'emp/employee.html', contex)