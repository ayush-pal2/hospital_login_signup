from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    user_type = forms.ChoiceField(choices=Profile.USER_TYPE)
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    pincode = forms.CharField(required=False)

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2',
            'user_type', 'profile_picture', 'address_line1', 'city', 'state', 'pincode'
        ]
