from django.db import models

# Create your models here.
class Blog_User(models.Model):
    user_name = models.CharField(max_length=20,default='demo')
    user_password = models.CharField(max_length=10,default="demo")

    def __str__(self):
        return self.user_name

class Post_Blog(models.Model):
    blog_image = models.ImageField(upload_to='blog_images',default='Add Please')
    title = models.CharField(max_length=100,unique=True)
    author = models.ForeignKey(Blog_User,on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    blog_like = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog_title = models.CharField(max_length=100,default='demo')
    name = models.CharField(max_length=20,default='demo')
    comment=models.CharField(max_length=100,default='demo')

    def __str__(self):
        return self.blog_title