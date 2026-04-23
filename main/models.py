from django.db import models

class Livraison(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ]

    nom_expediteur = models.CharField(max_length=100)
    nom_destinataire = models.CharField(max_length=100)
    adresse_livraison = models.CharField(max_length=255)
    telephone_destinataire = models.CharField(max_length=20)
    description_colis = models.TextField()
    poids_colis = models.DecimalField(max_digits=6, decimal_places=2)
    prix_livraison = models.DecimalField(max_digits=8, decimal_places=2)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_expediteur} -> {self.nom_destinataire}"