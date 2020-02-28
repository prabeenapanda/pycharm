from django.db import models
class rack(models.Model):
    name=models.CharField(max_length=10)
    size=models.CharField(max_length=10,null=True)

# Create your models here.
    def __str__(self):
         return self.name