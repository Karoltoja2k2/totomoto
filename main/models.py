from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Offer(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offer', null=True)

    title = models.CharField(max_length=200)
    mm = models.CharField(max_length=50, null=True)
    accident = models.BooleanField(null=True)
    price = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title

class Images(models.Model):
    offer = models.ForeignKey(Offer, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Images')
