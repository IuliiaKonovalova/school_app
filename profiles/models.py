from django.db import models


# Roles to assign to users
ROLES = (
        (0, 'boss'),
        (1, 'teacher'),
        (3, 'sales'),
        (4, 'receptionist'),
        (5, 'parent'),
        (6, 'potential user'),
)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    role = models.IntegerField(choices=ROLES, default=6)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name