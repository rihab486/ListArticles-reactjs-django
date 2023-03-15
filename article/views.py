from django.shortcuts import render

from rest_framework import generics
from .models import *
from article.serializers import *

#create and list article
class ArticleListCreate(generics.ListCreateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
#Update, list and list article
class ArticleupdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer

class ClassificationListCreate(generics.ListCreateAPIView):
    queryset=Classification.objects.all()
    serializer_class=ClassificationSerializer


class ClassificationupdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Classification.objects.all()
    serializer_class=ClassificationSerializer
