from django.shortcuts import render
from django.http import request

# Create your views here.
def home(request):
    lst=[]
    if request.method == "POST":
        num1=request.POST.get('num1')
        num2=request.POST.get('num2')
        oper=request.POST.get('oper')
        if oper == '+':
            lst.append(float(num1)+float(num2))

        if oper == '-':
            lst.append(float(num1)-float(num2))

        if oper == '*':
            lst.append(float(num1)*float(num2))

        if oper == '/':
            lst.append(float(num1)/float(num2))

        return render(request,'appcalci/home.html',{'lst':lst})
    return render(request,'appcalci/home.html')