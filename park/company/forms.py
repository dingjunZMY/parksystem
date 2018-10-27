from django import forms

class CompanyForm(forms.Form):
    company_name=forms.CharField(max_length=10,required=False)
    company_id=forms.CharField(max_length=50,required=False)

