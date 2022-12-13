from django.db import models

# Create your models here.


class People(models.Model):
    full_name = models.CharField(
        max_length=1024,
        verbose_name="Nombre completo")

    code = models.CharField(
        max_length=20,
        verbose_name="Cedula")
    
    email = models.EmailField()

    activated = models.BooleanField(default=False)
    timestamp = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} - {} - {}'.format(self.full_name, self.code, self.activated)