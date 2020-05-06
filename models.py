from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class ProfilePerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    
    isPsicologo = models.BooleanField(default=False)
    crp = models.CharField(max_length=10, blank=False)
    bio = models.TextField(max_length=500, blank=False)

@receiver(post_save, sender=User)
def update_user_profile_person(sender, instance, created, **kwargs):
    if created:
        ProfilePerson.objects.create(user=instance)
    instance.profileperson.save()


