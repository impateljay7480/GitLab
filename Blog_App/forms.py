from django import forms
from Blog_App.models import Post_Blog

class add_blog(forms.ModelForm):
    class Meta:
        model = Post_Blog
        fields = ('blog_image','title','author','content')
        widgets = {
            'blog_image':forms.FileInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }
