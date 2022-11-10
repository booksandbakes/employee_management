from re import search
from socket import fromshare
from typing import Tuple
from xml.dom import ValidationErr
from django import forms
from .models import Employee, Department

class Employee_Form(forms.ModelForm):

    class Meta:
        model = Employee
        fields = "__all__"
       
    def clean(self,*args, **kwargs):
        phone_no = self.cleaned_data.get('phone_no')
        print('\nPhno:',phone_no)
        if len(str(phone_no))!=10 and phone_no:
            raise forms.ValidationError('Invalid Phone number')
        return super(Employee_Form, self).clean(*args, **kwargs)
    


class Dept_Form(forms.Form):
    Department_name = forms.CharField(max_length=50, required=False)


class update_form(forms.ModelForm):
   
    class Meta:
        model = Employee
        fields = ('depart_ment',)

class search_form(forms.Form):
    searchfield = forms.CharField(max_length=50)
    optionfield = forms.ChoiceField(choices=((1,'Name'),(2,'Department'),(3,'Email')))