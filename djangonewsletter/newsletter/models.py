from django.db import models


class NewsletterSignup(models.Model):

    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        """Return the signup email."""
        return self.email
