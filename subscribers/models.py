from django.db import models

# Create your models here.


class Subscribers(models.Model):
    """A subscriber model"""

    email = models.CharField(max_length=100, blank=False,
                             null=False, help_text="Email address")
    full_name = models.CharField(
        max_length=200, blank=False, null=False, help_text="First and Last name")

    def __str__(self):
        """String repr of this object"""
        return self.full_name

    class Meta:  # noqa
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"
