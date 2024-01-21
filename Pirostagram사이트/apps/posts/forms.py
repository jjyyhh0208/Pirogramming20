from django import forms
from .models import Post

class NewPost(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(NewPost, self).__init__(*args, **kwargs)
        self.fields['writer'].disabled = True