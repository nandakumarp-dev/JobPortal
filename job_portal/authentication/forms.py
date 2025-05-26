from django import forms
from django.contrib.auth.models import User
from .models import EmployerProfile, JobSeekerProfile

class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username','email','password']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError("Passwords do not match")


class EmployerProfileForm(forms.ModelForm):

    class Meta:

        model = EmployerProfile
        exclude = ['custom_user','website']

class JobSeekerProfileForm(forms.ModelForm):

    class Meta:

        model = JobSeekerProfile
        exclude = ['custom_user']


