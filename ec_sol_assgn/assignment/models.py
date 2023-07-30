from django.db import models
from django.contrib.postgres.search import SearchVector, SearchVectorField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Define the SearchVectorField to support full-text search
    search_vector = SearchVectorField(null=True, blank=True)

    def __str__(self):
        return self.name

@receiver(post_save, sender=Place)
def update_search_vector(sender, instance, created, **kwargs):
    if created:
        # Only update the search_vector when a new instance is created
        instance.search_vector = SearchVector('name', 'description')
        Place.objects.filter(pk=instance.pk).update(search_vector=instance.search_vector)

