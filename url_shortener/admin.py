from django.contrib import admin
from .models import Url

# Register your models here.




class UrlAdmin(admin.ModelAdmin):
    list_display = ('short_url', 'long_url', 'user_id', 'is_public')

    class Meta:
        model = Url


admin.site.register(Url, UrlAdmin)
