# modules required to be imported for the creation of the form
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator
from django.forms import extras
from .models import UserProfile


# this is a modelForm
class UserForm(forms.ModelForm):
    # makes the field a password field.
    password = forms.CharField(widget=forms.PasswordInput)
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    # phone_number = forms.CharField(validators=[phone_regex])  # validators should be a list
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password"]


#class ChangePasswordForm(forms.ModelForm):
    # makes the field a password field.
   # password = forms.CharField(widget=forms.PasswordInput)
   # class Meta:
       ### def clean(self):
        #cleaned_data = super(ChangePasswordForm, self).clean()
        #password = cleaned_data.get("password")
        #confirm_password = cleaned_data.get("confirm_password")

        #if password != confirm_password:
           # raise forms.ValidationError(
               # "password and confirm_password does not match!"
           # )

class ProfileForm(forms.ModelForm):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    birth_date = forms.DateField(widget=forms.TextInput(attrs=
    {
        'class':'datepicker'
    }))
    gender = forms.ChoiceField(choices=GENDER_CHOICES,required=True)

    class Meta:
        model = UserProfile
        fields = ("address","birth_date","gender")


# a simple form not bound to a model
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
