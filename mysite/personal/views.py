from django.shortcuts import render

def index(request):
    return render(request,'personal/includes/home.html')

def contact(request):
    return render(request,'personal/basic.html',{'content':['if u like to contact','gmail']})
