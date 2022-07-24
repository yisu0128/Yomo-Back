#from xml.etree.ElementInclude import include
from django.urls import path, include
from rest_framework import routers

from b_pj_app.views import UserViewSet, PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)#users url에 UserViewSet 맵핑
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)) #http://127.0.0.1:8000/b_pj_app/users/
]