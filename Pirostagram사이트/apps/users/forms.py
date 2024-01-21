from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserSignUp(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('name', 'intro')
    
class UserUpdate(UserChangeForm):
    class Meta (UserChangeForm.Meta):
        model = User
        fields = ('username', 'name', 'intro')