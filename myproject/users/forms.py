from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['role', 'degree', 'major', 'current_role', 'experience_years', 'software_skills', 'music_skills', 'sports_skills']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        # Disable the role field if it has already been set
        if self.instance and self.instance.role:
            self.fields['role'].disabled = True  # Role is now read-only

        # Hide the degree and major fields unless the user is a student
        if self.instance.role != 'student':
            self.fields['degree'].widget = forms.HiddenInput()
            self.fields['major'].widget = forms.HiddenInput()

        # Hide the current role and experience fields unless the user is an employer
        if self.instance.role != 'employer':
            self.fields['current_role'].widget = forms.HiddenInput()
            self.fields['experience_years'].widget = forms.HiddenInput()
