from django import forms

class ProductForm(forms.Form):
    urun= forms.CharField(max_length = 200)
class ProductForm2(forms.Form):
    post2= forms.CharField(max_length = 200)