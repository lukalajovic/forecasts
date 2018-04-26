
from django import forms
class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100,error_messages={'required':'Write your name.'})
   password = forms.CharField(widget = forms.PasswordInput())
   error_messages = {'username': {'required': 'custom required message'}}
   class Meta:
      fields=['username','password']
      error_messages = {'username': {'required': 'custom required message'}}



class LoginForm(forms.Form):
   neki = forms.CharField(max_length = 100,error_messages={'required':'Write your name.'})

   class Meta:
      fields=['neki']
      error_messages = {'neki': {'required': 'custom required message'}}