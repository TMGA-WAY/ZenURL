from django.db import models
from django.utils.text import slugify


# Create your models here.

## URL model
class Url(models.Model):
    """
    This model is used to store the long URL, short URL, user ID, and whether the URL is public or not.
    :param short_url: Short URL
    :param long_url: Long URL
    :param user_id: User ID
    :param is_public: Is the URL public or not
    """
    short_url = models.CharField(max_length=50, unique=True)
    long_url = models.URLField(max_length=2000)
    user_id = models.IntegerField()
    is_public = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        """
        This method returns the string representation of the URL model.
        :return:
        """
        return f"Short URL: {self.short_url} \nLong URL: {self.long_url} \nUser ID: {self.user_id} \nIs Public: {self.is_public}"

    def save(self, *args, **kwargs):
        """
        This method is used to save the URL model.
        :param args:
        :param kwargs:
        :return:
        """
        self.slug = slugify(self.short_url)
        super().save(*args, **kwargs)
