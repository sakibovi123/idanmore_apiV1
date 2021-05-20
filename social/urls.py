from django.urls import path
from .views import *


urlpatterns = [
    path("posts/", APIPostView.as_view()),
]