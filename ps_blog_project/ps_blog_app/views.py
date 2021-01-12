from django.shortcuts import render
from ps_blog_app.models import category, blog_post, comment, User
from ps_blog_app.forms import comment_form, UserProfileInfoForm, login_form
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def blog_index(request):
    posts = blog_post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, 'ps_blog_app/blog_index.html', context)

# Login page view. 
def login_page(request): 
    logged_in = False
    logged_in_form = login_form()
    # If user tried to POST, authenticate their credentials.
    if request.method == 'POST': 
        logged_in_form = login_form(data=request.POST)
        username = request.POST.get('user_name')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        # If user is registered in database. 
        if user: 
            if user.is_active: 
                login(request, user)
                logged_in = True
                return HttpResponseRedirect(reverse('blog_index'))
        else: 
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
    
    elif logged_in == False and request.method != 'POST':
        return render(request, 'ps_blog_app/login.html', {'login_form':logged_in_form, 'logged_in':logged_in})

    else:
        logged_in = True 
        return render(request, 'ps_blog_app/login.html', {'login_form':logged_in_form, 'logged_in':logged_in})

# Used to add new users to be able to post blogs. 
def register(request): 
    registered = False
    if request.method == 'POST': 
        user_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid(): 
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            if 'profile_pic' in request.FILES: 
                profile.profile_pic = request.FILES['profile_pic']
            
    
            registered = True 
        else: 
            print(user_form.errors)
    else: 
        user_form = UserProfileInfoForm()
    
    return render(request, 'ps_blog_app/register.html', {'user_form': user_form,  'registered': registered})


def upcoming_titles(request): 
    return render(request, 'ps_blog_app/upcoming.html')

def blog_category(request, category): 
    # Use filter query to order the posts by the dates they were created on. 
    # The '-' infront of 'created_on' specifies to start with the largest value.
    posts = blog_post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    
    context = {
        "category": category, 
        "posts" : posts
    }

    return render(request, 'ps_blog_app/blog_category.html', context)

def blog_detail(request, pk):
    # Will be used as template var in blog_detail.html. 
    b_post = blog_post.objects.get(pk=pk)

    form = comment_form()
    # Check for post request in the server.
    if request.method == 'POST':
        # Create new comment if so.
        form = comment_form(request.POST)
        # Make sure all fields from comment() have been entered in correctly.
        if form.is_valid():
            new_comment = comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=b_post
            )
            new_comment.save()

    # Query database for all the comments assigned by the given post. 
    comments = comment.objects.filter(post=b_post)

    context = {
        "post": b_post,
        "comments": comments,
        "form": form,
    }
    return render(request, 'ps_blog_app/blog_detail.html', context)

