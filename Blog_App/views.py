from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from Blog_App.models import Post_Blog 
# Create your views here.

def index(request):
    all_blog = Post_Blog.objects.all()
    return render(request,'index.html',{'all_blog':all_blog})

def blog_detail(request,id):
    detail = get_object_or_404(Post_Blog,pk=id)
    return render(request,'view.html',{'detail':detail})