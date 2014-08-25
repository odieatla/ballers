from django import forms
#from django.forms import extras
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.admin import widgets
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from court.models import UserProfile
import logging
from datetime import datetime
logger = logging.getLogger(__name__)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username', '').lower()
        password = self.cleaned_data.get('password', '')

        logger.debug(username)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                self.user = user
            else:
                raise forms.ValidationError(_("User is not active"))
        else:
            raise forms.ValidationError(_("Invalid login."))

        return self.cleaned_data

class SignupForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$',
                                max_length=30,
                                required=True,
                                widget=forms.TextInput(),
                                label=_(u'Username'),
                                error_message={
                                    'required': 'Please enter a user name',
                                    'invalid': 'You username may only contain letters and numbers'
                                })
    email = forms.EmailField(widget=forms.TextInput(),
                             required=True,
                             max_length=75,
                             label=_(u'Email'),
                             error_messages={
                                 'required': 'Please enter an email'
                             })
    password = forms.CharField(widget=forms.PasswordInput(),
                               label=_(u'Password'),
                               required=True
                               )
    password_confirm = forms.CharField(widget=forms.PasswordInput(),
                                       label=_(u'Password'),
                                       required=True
                                       )

    birthdate = forms.DateField(widget=SelectDateWidget,
                                label=_(u'Birthdate'))
    def clean_username(self):
        username = self.cleaned_data["username"]
        user = User.objects.filter(Q(username__iexact=username))
        if not user.exists():
            return self.cleaned_data["username"]
        raise forms.ValidationError(_("Username unavailable."))

    def clean_email(self):
        email = self.cleaned_data["email"]
        user = User.objects.filter(Q(email__iexact=email))
        if not user.exists():
            return self.cleaned_data["email"]
        raise forms.ValidationError(_("A user is registered with this email address."))

    def clean(self):
        if "password" in self.cleaned_data and "password_confirm" in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
                raise forms.ValidationError(_("Passwords are not match."))
        return self.cleaned_data

    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        email = self.cleaned_data.get('email', None)
        birthdate = self.cleaned_data['birthdate']

        new_user = User(username=username)
        new_user.set_password(password)
        new_user.is_active = False
        new_user.email = email
        new_user.save()

        new_up = UserProfile(user=new_user)
        new_up.birthdate = birthdate
        new_up.save()

        new_user = authenticate(username=username,
                                password=password)

        return new_user
