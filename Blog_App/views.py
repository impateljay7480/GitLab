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

def editblog(request,id):
    blog_edit = get_object_or_404(Post_Blog,pk=id)
    edit_blog_form = add_blog(request.POST or None,instance=blog_edit)
    if edit_blog_form.is_valid():
        edit_blog_form.save()
        return redirect(f'/view/{id}/')
    return render(request,'add_blog.html',{'edit_blog_form':edit_blog_form})

def like(request,id):
    post = get_object_or_404(Post_Blog,pk=id)
    update = Post_Blog.objects.filter(pk=id).update(blog_like= int(post.blog_like)+1)
    return redirect(f'/view/{id}/')