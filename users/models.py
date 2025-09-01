from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.

class User0(models.Model):
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=500, unique=True, blank=True, null=True)
    adress = models.TextField(max_length=500, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="static/images/profiles/", default="profiles/default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.username)
    
    
    
    
    
    
    
    
    
    
#      Signals
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = User0.objects.create(
            username = user.username,
            email = user.email,
            name = user.first_name + " " + user.last_name,
            adress = user.address,
            profile_image = user.profile_image  # Assuming User has profile_image field
        )

    
def deleteProfile(sender, instance, **kwargs):
    print('Delete Profile....')
    print('instance:', instance)

@receiver(post_save, sender=User0)    
def updateProfile(sender, instance, created, **kwargs):
    print('Update Profile')
    print('instance:', instance)
    print('created:', created)
    
#post_save.connect(updateProfile, sender=User0)
#post_delete.connect(deleteProfile, sender=User0)