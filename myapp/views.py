from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def trial(request):
    return HttpResponse("<h1>Project is on air</h1>")

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"myapp/home.html")

def profile(request):
    name="Pradeep"
    contact="7204942247"
    email="pradeephuded37@gmail.com"
    return render(request,"myapp/profile.html",{'name':name,'contact':contact,'email':email})

def get_demo(request):
    name=request.GET.get('name')
    return render(request,"get_demo.html",{'name':name})


def post_demo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        return HttpResponse("<h1>Thanks for submission Mr. {}</h1>".format(name))
    return render(request,"post_demo.html")