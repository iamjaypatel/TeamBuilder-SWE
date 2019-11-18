from django import forms

class createProjForm(forms.Form):
    proj_name = forms.CharField(label='Project name', max_length=60)
    proj_descr = forms.CharField(widget=forms.Textarea, max_length=300)
