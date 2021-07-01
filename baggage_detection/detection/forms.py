from django import forms
from .models import ImageModel
from django.contrib.auth.models import User


class ImageForm(forms.ModelForm):
    # image = forms.ImageField()
    class Meta:
        model = ImageModel
        fields = ('image',)
    #
    # def save_src_img(self, image):
    #     src_img = ImageModel(image=image)
    #     src_img.save()
    #     return src_img
    #
    # def save_mod_img(self, image):
    #     mod_img = ImageModel(image=image)
    #     mod_img.save()
    #     return mod_img
