from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer

from rest_framework.permissions import IsAuthenticated
from djoser.views import UserViewSet as DjoserUserViewSet
from .serializers import UserSerializer

# Create your views here.
# Exemple de  vue pour recuperer tous les articles publies sans django Restframework
def liste_articles(request):
    articles = Article.objects.filter(est_publie=True)
    return render(request, 'blog/liste_articles.html',{'articles': articles})


# une vue Django REST framework affichant de tous les articles de blog publie
class ListeArticlesAPI(generics.ListAPIView):
    queryset = Article.objects.filter(est_publie=True)
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    


class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleUpdateView(generics.UpdateAPIView):
      queryset = Article.objects.all()
      serializer_class = ArticleSerializer
      lookup_field = 'id'  

class ArticleDeleteView(generics.DestroyAPIView):
     queryset = Article.objects.all()
     serializer_class = ArticleSerializer
     lookup_field = 'id'


