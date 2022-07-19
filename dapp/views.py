from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Colors
# Create your views here.

def index(request):
    c_name="test"
    num=str(3)
    if request.method == "POST":
        c_name=request.POST['selection']
        num=request.POST['num']
        print(c_name)
        print(num)
        # col = Colors(color_red=num)
        # col.save()
    return render(request, "index.html",{'color_name':c_name,'color_num':num})