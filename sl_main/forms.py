from django.forms import ModelForm
from .models import *

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()

class ItemForm(ModelForm):
    class Meta:
        model = ItemProject
        fields = '__all__'
        #['','']