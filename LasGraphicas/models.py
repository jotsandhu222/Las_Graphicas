from django.db import models
import uuid
from django.contrib.auth.models import User
    
class Polo(models.Model):
    type_choices = [
        ('polo', 'Polo'),
        ('round', 'Round Neck'),
    ]
    ideal_for_choices = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('kids', 'Kids'),
        ('other', 'Other'),
    ]
    fabric_choices = [
        ('Bio Wash Cotton', 'Bio Wash Cotton'),
        ('Honeycomb Cotton', 'Honeycomb Cotton'),
        ('polyester', 'Polyester'),
        ('wool', 'Wool'),
        ('other', 'Other'),
    ]
    
    fit_choices = [
        ('Loose', 'Loose'),
        ('Regular', 'Regular'),
    ]
    size_choices = [
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
    ]
    pattern_choices = [
        ('printed', 'Printed'),
        ('plain', 'Plain'),
        ('embroidary', 'Embroidary'),
    ]
    sleeve_choices = [
        ('3/4', '3/4'),
        ('Full', 'Full'),
        ('Half', 'Half'),
    ]
    occasion_choices=[
        ('casual', 'Casual'),
        ('formal', 'Formal'),
        ('sports', 'Sports'),
        ('party', 'Party'),
    ]
    fabric_care_choices = [
        ('dontIron', "Do not Iron on Print/Embroidary/embellishment"),
        ('regular', 'Regular Machine Wash'),
    ]
   
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, default="")
    market_price = models.IntegerField(default=999)
    selling_price = models.IntegerField(default=699)
    fabric_weight = models.CharField(max_length=50, default='250 g')
    occasion = models.CharField(max_length=20, choices=occasion_choices, default='casual')
    pattern = models.CharField(max_length=50, choices=pattern_choices, default='printed')
    polo_sleeve = models.CharField(max_length= 20, choices=sleeve_choices, default='Half')
    polo_fit = models.CharField(max_length=50, choices=fit_choices, default='Loose')
    fabric_care = models.CharField(max_length=50, choices=fabric_care_choices, default='regular')
    fabric = models.CharField(max_length=50, choices=fabric_choices, default='Bio Wash Cotton')
    size = models.CharField(max_length=10, choices=size_choices, default='l')   
    ideal_for = models.CharField(max_length=20, choices=ideal_for_choices, default='men')
    quantity = models.IntegerField(default=1)
    tshirt_type = models.CharField(max_length=20, choices=type_choices, default='polo')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)
    
    def __str__(self):
        return f'{self.name}' #{self.description} {self.market_price} {self.selling_price} {self.polo_sleeve}'
    
    class Meta:
        ordering = ['-created']
    
    
class PoloImage(models.Model):
    polo = models.ForeignKey(Polo, related_name = 'images', on_delete= models.CASCADE)
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    



class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlists')
    product = models.ForeignKey(Polo, on_delete=models.CASCADE, related_name='wishlists')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Ensure a user can't add the same product twice

    def __str__(self):
        return f"{self.user.username}'s wishlist - {self.product.name}"
    
    
class Homepage(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, default="home-page")
    brand_logo = models.ImageField(upload_to='static/images/homepage', blank=True, null=True)
    main_image = models.ImageField(upload_to='static/images/homepage', blank=True, null=True)
    main_heading = models.TextField(max_length=255, blank=True, null=True)
    main_description = models.TextField(max_length=500, blank=True, null=True)
    first_image = models.ImageField(upload_to='static/images/homepage', blank=True, null=True)
    first_heading = models.TextField(max_length=255, blank=True, null=True)
    first_description = models.TextField(max_length=500, blank=True, null=True)
    second_image = models.ImageField(upload_to='static/images/homepage', blank=True, null=True)
    second_heading = models.TextField(max_length=255, blank=True, null=True)
    second_description = models.TextField(max_length=500, blank=True, null=True)
    third_image = models.ImageField(upload_to='static/images/homepage', blank=True, null=True)
    third_heading = models.TextField(max_length=255, blank=True, null=True)
    third_description = models.TextField(max_length=500, blank=True, null=True)
    fourth_image = models.ImageField(upload_to='static/images/homepage', blank=True, null=True)
    fourth_heading = models.TextField(max_length=255, blank=True, null=True)
    fourth_description = models.TextField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject