from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Article

# Create your tests here.
class PostAPITestCase(APITestCase):

    def setUp(self):
        # Creer un utilisateur pour l'auteur
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Creer un article publie pour le test
        Article.objects.create(
            titre ='Article 1',
            contenu = 'Article sur le clean code et low code',
            auteur=self.user,
            est_publie=True
        )
    
    def test_get_posts_returns_200(self):
        # Authentifier l'utilisateur (si necessaire)
        self.client.force_authenticate(user=self.user)

        # Effectuer une GET vers l'endpoint /api/posts/
        response = self.client.get('/api/posts/')

        # Verifier si la reponse a un statut code 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)