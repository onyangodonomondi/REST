from django.db import models

class Drink(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=20, decimal_places=3)
    description=models.TextField()

    def __str__(self):
        return self.name

