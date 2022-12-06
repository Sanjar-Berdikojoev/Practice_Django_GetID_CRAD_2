from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.PC_Details
        fields = '__all__'