from django.db import models

class PC_Details(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    price = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    more_button = models.CharField(max_length=1, null=True)
    description_1 = models.TextField(null=True)

    def __str__(self):
        return self.title
# Create your models here.
