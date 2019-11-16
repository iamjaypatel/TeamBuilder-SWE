from django import forms

class editProfForm(forms.Form):
    prof_firstName = forms.CharField(label='First name', max_length=60)
    prof_lastName = forms.CharField(label='Last name', max_length=20)
    prof_Email = forms.CharField(label='Email', max_length=20)