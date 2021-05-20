from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import Post
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response


def homeView(request):
    return render(request, 'Main/home.html')


class APIPostView(APIView):
    def get(self, request):
        posts = Post.objects.all()

        data = []
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

