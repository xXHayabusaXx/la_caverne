from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Personnages(model.Model):
    "Record person model"

    nom = models.CharField(max_length=50)
    age = models.IntegerField()
    sex = models.BooleanField()
    taille = models.IntegerField()
    poids = models.IntegerField()
    alignement = models.CharField(max_length=100)
    divinite = models.CharField(max_length=100)
    initiative = models.IntegerField()
    point_carac = models.IntegerField()


class Classe(model.Model):
    "Record classe model"

    nom = models.CharField(max_length=50)
    bonus_def = models.IntegerField()
    pdv = models.IntegerField()
    recuperation = models.IntegerField()


class Race(model.Model):
    "Record race model"

    nom = models.CharField(max_length=50)
    bonus_carac = models.IntegerField()
    vitesse_dep = models.IntegerField()
    cat_taille = models.CharField(max_length=50)
    vision = models.BooleanField()


class Def(model.Model):
    "Record definition model"

    nom = models.CharField(max_length=50)
    valeur = models.IntegerField()


class Carac(model.Model):
    "Record character model"

    nom = models.CharField(max_length=50)
    valeur = models.IntegerField()
