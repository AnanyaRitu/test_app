from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# Create your forms here.

class Log_in_form(AuthenticationForm):
    class Meta:
        model=User
        fields = ['username', 'password']



class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")


class ParentDataCreationForm(forms.Form):
	firstName = forms.CharField(label='First name', max_length=100)
	lastName = forms.CharField(label='Last name', max_length=100)
	street = forms.CharField(label='Street', max_length=100)
	city = forms.CharField(label='City', max_length=100)
	state = forms.CharField(label='State', max_length=100)
	zip = forms.CharField(label='Zip', max_length=100)


class ChildDataCreationForm(forms.Form):
	firstName = forms.CharField(label='First name', max_length=100)
	lastName = forms.CharField(label='Last name', max_length=100)