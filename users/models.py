"""User models"""

#Django
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import URLField

# Create your models here.
class Profile(models.Model):
    """Profile model.

    proxy model that extends the DB with other
    information
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Return username."""
        return self.user.username