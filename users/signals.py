from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# When a user is saved then send this signal and this is going to be received by this receiver
# and this receiver is this created_profile function and this create_profile function takes
# all of these arguments that our post_save sgnal pasts to it and one of those is the instance
# of the user and one of those is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # Also create a save_profile function that just save our profile every time the user object is saved
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # save the profile when the suer is created
    instance.profile.save()
