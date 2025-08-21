from django import forms

class RegisterForm(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    contact=forms.IntegerField()
    image=forms.ImageField()
    file=forms.FileField()