from django.db import models

# Create your models here.
class tb(models.Model):
    img = models.ImageField(upload_to='product')
    desc = models.TextField()
    field_name = models.URLField(max_length=200)

