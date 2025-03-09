from django.db import models

class TShirt(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Polo(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    market_price = models.IntegerField()
    selling_price = models.IntegerField()
    polo_sleeve = models.CharField(max_length= 200)
    polo_fit = models.CharField(max_length=200)
    fabric = models.CharField(max_length=200)
    ideal_for = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.name}' #{self.description} {self.market_price} {self.selling_price} {self.polo_sleeve}'
    
    
class PoloImage(models.Model):
    polo = models.ForeignKey(Polo, related_name = 'images', on_delete= models.CASCADE)
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    
class Product(models.Model):
    name = models.CharField(max_length=200)