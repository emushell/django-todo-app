from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task, Profile


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Add new task...'
        }
    ))

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user_profile']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


class CreateUserForm(UserCreationForm):
    pass

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
