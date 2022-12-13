from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(email='admin@mail.com').exists():
            user_object = User(username='admin', email='admin@mail.com', first_name='admin', last_name="super")
            user_object.set_password('admin')
            user_object.is_superuser = True
            user_object.is_staff = True

            user_object.save()

            print(">>> User with username: '{}' created".format('admin'))
            """/Users/yurley.sanchez/Dev/proyectos/seguimiento_recoleccion_firmas/myapp/management/commands/populate_usuarios.py"""