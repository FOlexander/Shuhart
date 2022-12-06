from django.db import models
from django.conf import settings


# Create your models here.

class Tables(models.Model):
    class Meta:
        verbose_name_plural = 'Tables'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_table = models.FileField(upload_to='media/')
    user_model = models.ImageField()

    def __repr__(self):
        return f'{self.user} chart'
