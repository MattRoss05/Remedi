from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from providers.models import Provider

@receiver(post_save, sender =CustomUser)
def create_provider(sender, instance, created, **kwargs):
    print('signal processed')
    if created and instance.user_type == 'provider':
        newProvider  = Provider(user=instance)
        newProvider.save()
        print(f"Provider created for {instance.username}")