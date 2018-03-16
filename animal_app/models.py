from django.db import models

# Create your models here.
class Animal(models.Model):
    name =  models.CharField(max_length=100)
    total_amount = models.IntegerField(default=0)

    def __str__(self):
        return '[{}] {}'.format(self.id, self.name)
