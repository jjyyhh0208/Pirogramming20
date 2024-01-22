from django import forms
from .models import *

class NewPost(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('__all__')
        exclude = ['writer', 'like', 'is_liked']

class NewComment(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('__all__')
