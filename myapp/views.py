from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail

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

def registrations(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("pwd")
        phno=request.POST.get("phno")
        date=request.POST.get("birthday_day")
        month=request.POST.get("birthday_month")
        year=request.POST.get("birthday_year")
        gender=request.POST.get("sex")
        if gender=="1":
            gender="FeMale"
        else:
            gender="Male"
        send_mail("Thanks For Registration","hello Mr./Ms.{} {}\n Thanks for Registering".format(first_name,last_name),
        "pradeephuded37@gmail.com",[email,],fail_silently=False)
        return redirect("home")
    return render(request,"myapp/registrations.html")

def multi(request):
    if request.method=="POST":
        foods=request.POST.getlist("food")
        languages=request.POST.getlist("language")
        return HttpResponse("<h1>{}{}<h1>".format(foods,languages))
    return render(request,'multiselect.html')

from django.core.files.storage import FileSystemStorage

def img_upload(request):            
    return render(request,"img_upload.html")


from myapp.utilities import storage_image
def img_display(request):
    file_url=False
    if request.method=="POST" and request.FILES:
        image1=request.FILES['sam1']
        image2=request.FILES['sam2']
        file_urls=map(storage_image,[image1,image2])
            
    
    return render(request,"img_display.html",context={'file_urls':file_urls})
    


