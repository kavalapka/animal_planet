from django.db import models

# Create your models here.
class Animal(models.Model):
    name =  models.CharField(max_length=100)
    number = models.IntegerField(default=0)

    def __str__(self):
        return '[{}] {}'.format(self.pk, self.name)
