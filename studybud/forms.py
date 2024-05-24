from django.forms import ModelForm
from .models import User, Room
from django.contrib.auth.forms import UserCreationForm as DefaultUserCreationForm


class UserCreationForm(DefaultUserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['topic', 'name', 'description']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'avatar', 'bio']
