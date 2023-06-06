from django.db import models

class Aisle(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
    
class Unit(models.Model):
    name = models.CharField(max_length=16)
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=128)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    quantity = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=128)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    aisle = models.ForeignKey(Aisle, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        ingredient = ""
        if self.aisle:
            ingredient += f"({self.aisle}) "
        ingredient += f"{self.quantity} {self.unit} {self.name}"
        return ingredient