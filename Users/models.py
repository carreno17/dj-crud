from django.db import models
from django.contrib.auth.models import User
from djangocrud.models import Categories
from django.db.models.signals import post_save


class LibraryCategory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="rlibrary")
    categories = models.ManyToManyField(Categories, blank=True)

    def __str__(self):
        return self.user.username

"""Funcion para que en el momento que un usuario se registre
se le cree inmediatamente la libreria"""
def post_save_user_receiver(sender, instance, created, **kwargs):
    if created:
        library=LibraryCategory.objects.create(user=instance)
        

post_save.connect(post_save_user_receiver, sender=User)



