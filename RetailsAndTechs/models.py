from django.db import models
from django.contrib.auth.models import User

class Retailer(models.Model):
    name = models.CharField(max_length=200)
    retailerrating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    def __str__(self):
        return self.name

class Technician(models.Model):
    name = models.CharField(max_length=200)
    technicianrating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    def __str__(self):
        return self.name

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE, null=True, blank=True)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, null=True, blank=True)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.score}"
