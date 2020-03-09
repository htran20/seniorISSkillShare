from allauth.account.forms import SignupForm
from .models import UserMentorProfile
from django import forms

class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # Add your own processing here.
        user_mentor_profile = UserMentorProfile(user=user, email=user.email, first_name=user.first_name,
                                                last_name=user.last_name)
        user_mentor_profile.save()

        # You must return the original result.
        return user