from django import forms
from .models import Post, Category
from .views import PasswordChangeForm
from django.contrib.auth.models import User

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for i in choices:
    choice_list.append(i)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippets', 'header_image')


        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value': ' ', 'id':'malko', 'type' : 'hidden'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Body'}),
            'snippets': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Body'}),
}
           

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippets')


        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Body'}),
            'snippets': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Body'}),}



class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'type': 'password'}))


    class Meta:
        model = User
        fields = ('old_password ', 'new_password1', 'new_password2')


