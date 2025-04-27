from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from providers.models import Provider


#this method is called everytime a custo user is made
@receiver(post_save, sender =CustomUser)
def create_provider(sender, instance, created, **kwargs):
    print('signal processed')
    #id the created user is of type provider
    if created and instance.user_type == 'provider':
        #make a new provider model entry in the database
        newProvider  = Provider(user=instance)
        newProvider.save()
        print(f"Provider created for {instance.username}")