from django import forms
from .models import Post_maqolas
from django_quill.forms import QuillFormField


class AddMaqolaForm(forms.Form):
    name = forms.CharField(max_length=150)
    content = QuillFormField()


class ChangeMaqolaForm(forms.ModelForm):
    class Meta:
        model = Post_maqolas
        fields = (
            'name',
            'quil',
        )
