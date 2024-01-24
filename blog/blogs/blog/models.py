from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_publication = models.DateTimeField(auto_now_add=True)
    est_publie = models.BooleanField(default=False)

    def __str__(self):
        return self.titre

