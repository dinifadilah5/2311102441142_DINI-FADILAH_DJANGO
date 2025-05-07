from django import forms
from blog.models import MyBlog

class ArtikelForm(forms.ModelForm):
    class Meta:
        model = MyBlog
        fields = ['judul','isi','kategori','thumbnail']
        widgets = {
            'judul': forms.TextInput(
                attrs={
                    'class': 'form-control'
            }),
            'isi': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'kategori': forms.Select(
                attrs={
                    'class': 'form-control'
                }),

        }