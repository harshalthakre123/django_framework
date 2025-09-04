from django import forms
from django.core.exceptions import ValidationError
from .models import User


# class RegisterForm(forms.Form):
#     name=forms.CharField(max_length=50)
#     email=forms.EmailField()
#     contact=forms.IntegerField()
#     image=forms.ImageField()
#     file=forms.FileField()

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'  
    
    def clean_name(self):
        print("end of name_Validation from forms.py")
        name =  self.cleaned_data.get('name')
        print(name)
        print(type(name))
        if len(name)==0:
            raise ValidationError("name field cannot be empty")
        
        elif name.isdigit():
            raise ValidationError("name should not contain number")
        
        elif name[0].isdigit():
            raise ValidationError("name should not start with a number")
        
        elif not (name.isalpha() and len(name)<20 and len (name)<3):
            raise ValidationError("name should only cantain letter and in btween 4 to 20 letter")
        return name