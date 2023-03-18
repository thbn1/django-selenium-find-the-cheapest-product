from django import forms
class ProductForm(forms.Form):
    post2= forms.CharField(max_length = 200)