from django.db import models


class Formapp(models.Model):
    Name = models.CharField(max_length=100)
    Message = models.TextField(max_length=100)

    def __str__(self):
        return self.Name
