from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm  # Assuming you have a form for creating blog posts


# def home(request):
#     return render(request,'blogApp/allblogs.html')


def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blogApp/allblogs.html', {'blog_posts': blog_posts})

def blog_detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    print(blog)
    return render(request, 'blogApp/singleBlog.html', {'blog': blog})

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user  # Assuming you have user authentication
            blog_post.save()
            return redirect('/blog/')
    else:
        form = BlogPostForm()

    return render(request, 'blogApp/createblog_form.html', {'form': form})
