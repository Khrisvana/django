from django.forms import widgets
from .models import Post
from django import forms 

class PostForm(forms.ModelForm):

    class Meta: 
        model = Post
        fields = ('author', 'title', 'text',)
        widgets = {
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'text' : forms.Textarea(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['author'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.sku
        else:
            return self.cleaned_data['author']