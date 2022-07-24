from django.contrib.auth.models import User
from rest_framework import serializers

from b_pj_app.models import Post, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class PostSerializer(serializers.ModelSerializer):
    writer = User.username
    class Meta: 
        model = Post
        fields =['title','content', 'created_time', 'writer' ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment
        fields = '__all__'
