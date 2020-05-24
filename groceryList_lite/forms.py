from django import forms
from .models import User,GroceryList,GrocerListContent,UsersAndGrocery
from .validation2 import EmailValidation,randomStringGenertor,verificationMail

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
        'email',
        'password',
        'securityQuestion',
        'securityQuesAnswer',
        ]
    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data["email"]
        EmailValidation.uniqueEmail(email)
        return email
        '''
        if len(User.objects.filter(email = email)) > 0:
            raise forms.ValidationError("Email should be unique")
        else:
            return email'''

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
        'email',
        'password'
        ]

#we can make this in signup form also as both are same but to not to be confused we are adding it
class ForgetPassword(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
        'email',
        'password',
        'securityQuestion',
        'securityQuesAnswer',
        ]

class GroceryListForm(forms.ModelForm):
    class Meta:
        model = GroceryList
        fields = [
        'title'
        ]

class GrocerListContentForm(forms.ModelForm):
    class Meta:
        model = GrocerListContent
        fields=['item']

class UsersAndGroceryForm(forms.ModelForm):
    class Meta:
        model = UsersAndGrocery
        fields = ['userId','canEdit','isAdmin']
    def clean_userExist(self,*args,**kwargs):
        email = self.cleaned_data["userId"].email
        if len(User.objects.filter(email = email))>0:
            return email
        return  forms.ValidationError("Email does not exist!")
