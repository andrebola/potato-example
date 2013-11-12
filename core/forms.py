from django import forms
from models import Post

class EditPost(forms.Form):
    title = forms.CharField(max_length = 300)
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':70}), label = 'Post',required=False)
    
    def __init__(self, user,post, *args, **kwargs):
        self.user = user
        super(EditPost, self).__init__(*args, **kwargs)
        self.fields['title'].initial = post.title
        self.fields['body'].initial = post.body

    def save(self,post):
        post.title = self.cleaned_data['title']
        post.body = self.cleaned_data['body']
        post.put()
        return post
    
class CreatePost(forms.Form):
    title = forms.CharField(max_length = 300)
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':70}), label = 'Post',required=False)

    def save(self):
        post=Post(title=self.cleaned_data['title'],body=self.cleaned_data['body'])
        post.put()
        return post