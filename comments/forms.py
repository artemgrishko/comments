from django import forms
from captcha.fields import CaptchaField

from .models import Comment


class CommentForm(forms.ModelForm):
    captcha=CaptchaField()

    class Meta:
        model = Comment
        fields = ['user_name', 'email', 'text', 'image', "text_file"]
