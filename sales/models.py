"""Models for the sales app"""
from django.db import models
from profiles.models import SalesManager, Parent


class Sales(models.Model):
    """Sales model"""
    sold_by = models.ForeignKey(
        SalesManager,
        on_delete=models.CASCADE,
        related_name='sold'
    )
    sold_to = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
        related_name='bought'
    )
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    student_id = models.IntegerField(default=0)

    def __str__(self):
        """Return string representation of sales."""
        return (
          str(self.sold_by) +
          ' sold ' +
          str(self.amount) +
          ' classes to ' +
          str(self.sold_to)
        )

    class Meta:
        """Meta class"""
        db_table = 'sales'
        ordering = ['-date']
