from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return self.text


class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return "{}{}".format(self.date, self.amount)
