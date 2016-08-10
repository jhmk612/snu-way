from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "vehicle",
            "price",
            "content",
            "publish",

            # 지도
            # 캘린더
        ]
