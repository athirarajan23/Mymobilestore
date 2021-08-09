from django.shortcuts import render,redirect

from . import forms
from .forms import MobileCreationForm,BrandCreationForm,BrandSearch
from .models import Brand,Mobile
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,"index.html")

def mobile_create(request):
    context={}
    form=MobileCreationForm()
    context["form"]=form
    if request.method=="POST":
        form=MobileCreationForm(request.POST,request.FILES) #to get image file
        if form.is_valid():
            form.save()
            messages.success(request,"Mobile Created")
            return redirect("addmobiles")
        else:
            messages.error(request,"Mobile not added")
            context["form"] = form
            return render(request, "mobile_create.html", context)

    return render(request,"mobile_create.html",context)

def mobile_list(request):
    mobiles=Mobile.objects.all()
    context={"mobiles":mobiles}
    return render(request,"list_mobile.html",context)

def mobile_update(request,id):
    mobile=Mobile.objects.get(id=id)
    form=forms.MobileUpdationForm(instance=mobile)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.MobileUpdationForm(mobile,request.FILES,instance=mobile)
        if form.is_valid():
            form.save()
            return redirect("listmobiles")
        else:
            return render(request, "mobile_edit.html", {"form": form})

    return render(request,"mobile_edit.html",{"form":form})



def brand_create(request):
    form=BrandCreationForm()
    context={"form":form}
    if request.method=="POST":
        form=BrandCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("addbrands")
    return render(request,"brand_add.html",context)

def list_brand(request):
    brands=Brand.objects.all()
    context={}
    context["brands"]=brands
    form=BrandSearch()
    context["form"]=form
    if request.method=="POST":
        form=BrandSearch(request.POST)
        if form.is_valid():
            brand_name=form.cleaned_data["brand_name"]
            brands=Brand.objects.filter(brand_name__contains=brand_name)
            context["brands"]=brands
            return render(request,"brand_list.html",context)
        else:
            context["form"] = form
            return render(request, "brand_list.html", context)

    return render(request,"brand_list.html",context)

def view_brand(request,id):
    brand=Brand.objects.get(id=id)
    context={"brand":brand}
    return render(request,"view_brand.html",context)

def remove_brand(request,id):
    brand=Brand.objects.get(id=id)
    brand.delete()
    return redirect("brandlist")

def update_brand(request,id):
    brand=Brand.objects.get(id=id)
    form=BrandCreationForm(instance=brand)
    context={"form":form}
    if request.method=="POST":
        form=BrandCreationForm(instance=brand,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("brandlist")
    return render(request,"update_brand.html",context)

def mobile_detail(request,id):
    mobile=Mobile.objects.get(id=id)
    context={"mobile":mobile}
    return render(request,"mobile_detail.html",context)


def remove_mobile(request,id):
    mobile=Mobile.objects.get(id=id)
    mobile.delete()
    return redirect("listmobiles")
