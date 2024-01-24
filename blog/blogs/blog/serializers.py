from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article


class UserCreateSerializer(DjoserUserCreateSerializer):
    class Meta(DjoserUserCreateSerializer.Meta):
        model = get_user_model()
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name')

class UserSerializer(serializers.ModelSerializer):        
     class Meta:
         model = get_user_model()
         fields = ('id', 'email', 'username', 'first_name', 'last_name')

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ['id','titre', 'contenu', 'auteur', 'date_publication', 'est_publie']
