from django import forms

class Park1Form(forms.Form):
    park_name=forms.CharField(max_length=20,required=False)
    park_id=forms.CharField(max_length=50,required=False)
