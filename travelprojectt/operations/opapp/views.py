

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def demo(request):
    name="math operations"
    return render(request, "index.html",{'obj':name})

def addition(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    result=x+y
    result1=x-y
    result2=x*y
    result3=x/y
    return render(request,"result.html",{'result':result,'result1':result1,'result2':result2,'result3':result3})


