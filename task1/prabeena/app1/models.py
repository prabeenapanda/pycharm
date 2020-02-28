from django.db import models
class student(models.Model):
    name=models.CharField(max_length=10)
    classes=models.CharField(max_length=10, null=True)
    age = models.IntegerField(null=True, blank=True)
    # s_id=models.IntegerField()


    def __str__(self):
        return self.name

