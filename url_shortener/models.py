from django.db import models


# Create your models here.

## URL model
class Url(models.Model):
    short_url = models.CharField(max_length=50, unique=True)
    long_url = models.URLField(max_length=2000)
    user_id = models.IntegerField()
    is_public = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return f"Short URL: {self.short_url} \nLong URL: {self.long_url} \nUser ID: {self.user_id} \nIs Public: {self.is_public}"
