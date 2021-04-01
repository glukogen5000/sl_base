from django.forms import ModelForm
from .models import *
from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file', 'description',  'item_proj', 'user_upload']


# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()

class ItemForm(ModelForm):
    class Meta:
        model = ItemProject
        fields = ['access', 'foto_montaj_upload', 'rtk_ready', 'act_ready', 'plan_data_ready_smr', 'komentariy']


class ItemFullForm(ModelForm):
    class Meta:
        model = ItemProject
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'author', 'item_p']
