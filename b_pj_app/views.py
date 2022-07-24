from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

from b_pj_app.serializers import UserSerializer, PostSerializer, CommentSerializer
from .models import Post, Comment


#from b_pj.urls import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer