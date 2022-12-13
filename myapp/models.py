from django.db import models

# Create your models here.


class People(models.Model):
    full_name = models.CharField(
        max_length=1024,
        verbose_name="Nombre completo")

    code = models.CharField(
        max_length=20,
        verbose_name="Cedula")
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    mobile = models.CharField(
        max_length=20,
        verbose_name="celular"
    )

    activated = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} - {} - {}'.format(self.full_name, self.code, self.activated)