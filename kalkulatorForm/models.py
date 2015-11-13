from django.db import models

# Create your models here.
class Typ(models.Model):
    KWADRAT = 0
    L = 1
    T = 2
    TYP_DESKI = (
        (KWADRAT, 'Kwadrat'),
        (L, 'L'),
        (T, 'T'),
    )

class Zamowienie(models.Model):
    l1 = models.FloatField(blank='True', null='True')
    l2 = models.FloatField(blank='True', null='True')
    l3 = models.FloatField(blank='True', null='True')
    l4 = models.FloatField(blank='True', null='True')
    l5 = models.FloatField(blank='True', null='True')
    l6 = models.FloatField(blank='True', null='True')
    listwa1 = models.NullBooleanField(blank='True', null='True')
    listwa2 = models.NullBooleanField(blank='True', null='True')
    listwa3 = models.NullBooleanField(blank='True', null='True')
    listwa4 = models.NullBooleanField(blank='True', null='True')
    listwa5 = models.NullBooleanField(blank='True', null='True')
    listwa6 = models.NullBooleanField(blank='True', null='True')
    listwa7 = models.NullBooleanField(blank='True', null='True')
    listwa8 = models.NullBooleanField(blank='True', null='True')
   # typ = Typ.KWADRAT

def __str__(self):
    return self.typ

