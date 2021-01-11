from django.shortcuts import render
from ps_blog_app.models import category, blog_post, comment
from ps_blog_app.forms import comment_form

# Create your views here.
def blog_index(request):
    posts = blog_post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, 'ps_blog_app/blog_index.html', context)


def login_page(request): 
    return render(request, 'ps_blog_app/login_page.html')


def upcoming_titles(request): 
    return render(request, 'ps_blog_app/upcoming.html')

def blog_category(request, category): 
    # Use filter query to order the posts by the dates they were created on. 
    # The '-' infront of 'created_on' specifies to start with the largest value.
    posts = blog_post.objects.filter(categories_name_contains=category).order_by('-created_on')
    context = {
        "category": category, 
        "posts" : posts
    }

    return render(request, 'ps_blog_app/blog_category.html', context)

def blog_detail(request, pk):
    # Will be used as template var in blog_detail.html. 
    post = blog_post.objects.get(pk=pk)

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
                post=post
            )
            new_comment.save()

    # Query database for all the comments assigned by the given post. 
    comments = comment.objects.filter(post=post)

    context = {
        "posts": post,
        "comments": comments,
        "form": form,
    }
    return render(request, 'ps_blog_app/blog_detail.html', context)