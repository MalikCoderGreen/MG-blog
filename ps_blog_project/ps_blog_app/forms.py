from django import forms
from ps_blog_app.models import UserProfileInfo, blog_post
from django.contrib.auth.models import User


# To allow registered users to create a post. 
class create_blog_form(forms.Form): 
    title = forms.CharField(max_length=60, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder" : "Your post name"
    })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
        "class": "form-control",
        "placeholder": "Create your post!"
    })
    )

        

# Form for commenting on a blog post.
class comment_form(forms.Form): 
    author = forms.CharField(max_length=60, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder" : "Your name"
    })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
        "class": "form-control",
        "placeholder": "Leave a comment!"
    })
    )

# Login form for login.html.
class login_form(forms.Form): 
    
    user_name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={
        "class" : "form-control",
        "placeholder" : "username",
    }), label='username')

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class" : "form-control",
        
    }), label='password')

     

# User profile form for registration page.
class UserProfileInfoForm(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class" : "form-control",
    }), label='password')

    class Meta(): 
        model = User
        help_texts = {
            'username' : None,
        }

    
        fields = ('username', 'email')
        widgets = {
            'username' : forms.TextInput(attrs={
                'class' : u'form-control',   
            }),

            'email' : forms.TextInput(attrs={
                'class' : u'form-control',
            }) 
        
        }

        
        labels = {
            'username' : 'username',
            'email' : 'email',
            'password' : 'password',
        }
        
        