'''
Author: BOA·Hankokku & Nico·Robin
Time: 2021/10/30 13:37

'''
from django.shortcuts import render


def runoob(request):
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    return render(request, "runoob.html", {"views_str": views_str})


def console(request):
    return render(request,'home/console.html')


def index(request):
    return render(request,'index.html')