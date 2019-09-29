from django.db import models


class Book(models.Model):
    def __str__(self):
        return self.name + '_' + self.author
        return self.price

    name  = models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    pulisher = models.CharField(max_length=100)
    Qty = models.CharField(max_length=100)






