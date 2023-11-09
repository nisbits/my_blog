from email.policy import default
from django import forms
from .models import *
from django.contrib.auth.models import User
# from accounts.models import profile
class BlogPostForm( forms.ModelForm ) :
    class Meta :
        model = BlogPost
        exclude =['author']

    
