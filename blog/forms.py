
from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', )

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput())
    last_name = forms.CharField(max_length=50, widget=forms.TextInput())
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def clean_username(self):
        uname = self.cleaned_data.get('username')
        try:
            usr = User.objects.get(username=uname)
        except:
            usr = False
        if usr:
            raise forms.ValidationError('Username already taken.', code='username-invalid')
        return uname

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Add a comment'}),
        }

