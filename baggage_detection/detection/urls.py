from django.urls import path, include
from django.conf.urls.static import static
import os
import sys
from . import views

sys.path.append(os.path.abspath('..'))
# from ..baggage_detection.settings import DEBUG, MEDIA_ROOT, MEDIA_URL

# from django.conf import settings

urlpatterns = [
    path('', views.ImageView.as_view(), name='main'),
    path('about', views.about, name='about'),
]
# print(MEDIA_ROOT)
# if DEBUG:
#     urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
