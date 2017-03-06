from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ArtistaFavorit(models.Model):
    id_artista = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    usuari = models.ForeignKey(User)