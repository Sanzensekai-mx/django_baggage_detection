from django.db import models
from django.conf import settings
from .detector import DetectorTF2
import os
import cv2
import os
import numpy as np
import tensorflow as tf
from object_detection.utils import label_map_util


def upload_to(instance, filename):
    return os.path.join(settings.MEDIA_ROOT, 'images', filename)


# Create your models here.
class ImageModel(models.Model):
    image = models.ImageField(upload_to='images', verbose_name='Изображение')

    def __str__(self):
        return f'Имя: {self.image.name.split("/")[-1]}'
