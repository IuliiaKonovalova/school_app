from django.db import models
from profiles.models import SalesManager, Parent


class Sales(models.Model):
    """Sales model"""
    sold_by = models.ForeignKey(SalesManager, on_delete=models.CASCADE)
    sold_to = models.ForeignKey(Parent, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
