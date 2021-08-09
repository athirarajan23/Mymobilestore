from django import forms
from django.forms import ModelForm
from .models import Mobile,Brand

class MobileCreationForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"
        widgets={
            "mobile_name":forms.TextInput(attrs={"class":"form-control"}),
            "brand": forms.Select(attrs={"class": "form-select"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "memory": forms.TextInput(attrs={"class": "form-control"}),
            "os": forms.TextInput(attrs={"class": "form-control"}),
            "specs": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }

class BrandCreationForm(ModelForm):
    class Meta:
        model=Brand
        fields="__all__"
        widgets={
            "brand_name":forms.TextInput(attrs={"class":"form-control"})
        }

class BrandSearch(forms.Form):
    brand_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}))



class MobileUpdationForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"
        widgets={
            "mobile_name":forms.TextInput(attrs={"class":"form-control"}),
            "brand": forms.Select(attrs={"class": "form-select"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "memory": forms.TextInput(attrs={"class": "form-control"}),
            "os": forms.TextInput(attrs={"class": "form-control"}),
            "specs": forms.TextInput(attrs={"class": "form-control"}),
        }