
from django.shortcuts import render,redirect, get_object_or_404
from .models import *

def create(request):
    if request.method == "POST":
        fullname=request.POST.get("fullname")
        profession=request.POST.get("profession")
        email=request.POST.get("email")
        mobilenumber=request.POST.get("mobilenumber")
        city=request.POST.get("city")
        address=request.POST.get("address")
        status=request.POST.get("status")
        profile=request.FILES.get("profile")
        profile = request.FILES.get("profile")
        if not profile:  
            profile = "images/default.jpg"
        
        
        if all([fullname,profession,email,mobilenumber,city,address,status,profile]):
            Directory.objects.create(
                fullname=fullname,
                profession=profession,
                email=email,
                mobilenumber=mobilenumber,
                city=city,
                address=address,
                status=status,
                profile=profile,
                
                )
            return redirect("create")
    data=Directory.objects.all()
    return render(request,"detail.html",{"data":data})
            
def edit(request, id):
    person=get_object_or_404(Directory, id=id)
    
    if request.method == "POST":
        person.fullname=request.POST.get("fullname")
        person.profession=request.POST.get("profession")
        person.email=request.POST.get("email")
        person.mobilenumber=request.POST.get("mobilenumber")
        person.city=request.POST.get("city")
        person.address=request.POST.get("address")
        person.status=request.POST.get("status")
        if request.FILES.get("profile"):
            person.profile = request.FILES["profile"]
        person.save()
        return redirect("create")
    data=Directory.objects.all()
    return render(request,"detail.html",{"data":data,"person":person})      

def delete(request,id):
    record=get_object_or_404(Directory, id=id)
    record.delete()
    return redirect("create")



