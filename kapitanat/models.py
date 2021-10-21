from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Jacht(models.Model):
    model = models.CharField(max_length=100)
    nazwa = models.CharField(max_length=100)
    rok_produkcji = models.IntegerField(default=2137)
    status = models.IntegerField(default=-1)
    data_dodania = models.DateTimeField(default=timezone.now)
    opis = models.TextField(default='#')
    # autor = models.ForeignKey(User)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('jacht-detail', kwargs={'pk': self.pk})

    