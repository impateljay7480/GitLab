from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from Blog_App.models import Post_Blog 
from Blog_App.forms import add_blog

# Create your views here.

def index(request):
    all_blog = Post_Blog.objects.all()
    return render(request,'index.html',{'all_blog':all_blog})

def blog_detail(request,id):
    detail = get_object_or_404(Post_Blog,pk=id)
    return render(request,'view.html',{'detail':detail})

def delete(request,id):
    post = get_object_or_404(Post_Blog,pk=id)
    post.delete()
    return redirect('/')

def addblog(request):
    add_blog_form = add_blog(request.POST,request.FILES)
    if add_blog_form.is_valid():
        add_blog_form.save()
        return redirect('/')
    return render(request,'add_blog.html',{'add_blog_form':add_blog_form})