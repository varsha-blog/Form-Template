from django.db import models


class Customer(models.Model):
    cid = models.CharField(max_length=7)
    name = models.CharField(max_length=20)
    address = models.TextField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
