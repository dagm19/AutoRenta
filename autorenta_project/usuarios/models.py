from django.db import models
from django.contrib.auth.models import AbstractUser

ROL_CHOICES = [
    ("Administrador", "Administrador"),
    ("Gerente", "Gerente"),
    ("Ventas", "Ventas"),
    ("Tecnicos", "Técnicos"),
    ("Cliente", "Cliente"),
]

class UserCustom(AbstractUser):
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default="Cliente", blank=True, null=True)
    #avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if self.rol == "Administrador":
            self.is_superuser = True
            self.is_staff = True
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'users'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
