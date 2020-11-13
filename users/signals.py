from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile,Address


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('User Created ..........!')


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    print('user Updated...!')
 

@receiver(post_save, sender=User)
def create_address(sender, instance, created, **kwargs):
	if created:
		Address.objects.create(users=instance)
		print("Address Created...!")


@receiver(post_save, sender=User)
def save_Address(sender,instance,created ,**kwargs):
	instance.address.save()
	print('address updated..!')