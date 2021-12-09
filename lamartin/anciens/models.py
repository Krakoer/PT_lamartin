from django.db import models
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from .validators import validate_letters, validate_alpha


# Create your models here.

class Ancien(models.Model):
    nom = models.CharField(max_length=20, validators=[validate_letters])
    prenom = models.CharField(max_length=20, validators=[validate_letters])
    ecole = models.CharField(max_length=20, validators=[validate_alpha])
    promo = models.IntegerField(default=0, validators=[MaxValueValidator(2023), MinValueValidator(2000)])
    specialite = models.CharField(max_length=40, validators=[validate_alpha])
    entreprise = models.CharField(max_length=30, validators=[validate_alpha], default="", blank=True)
    description = models.TextField(max_length=2000, validators=[validate_alpha])
    contact = models.CharField(max_length=25, default="", blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}, promo {self.promo}"


class AncienForm(ModelForm):
    class Meta:
        model = Ancien
        fields = ['nom', 'prenom', 'ecole', 'promo', 'specialite', 'entreprise', 'description', 'contact']
