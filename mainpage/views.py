from django.shortcuts import render
from . import models

def mainpage_all(request):
    post = models.PC_Details.objects.all()
    return render(request, 'index.html',{'post':post})

def detail(request, id):
    post = models.PC_Details.objects.get(id=id)
    return render(request, 'index2.html', {'post': post})
# Create your views here.
