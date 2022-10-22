from enum import auto
from venv import create
from django.db import models
f"""rom django.contrib.auth.models import User

from home.help import forget_pass
# Create your models here.



class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    forget_pass_token=models.CharField(max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.user.username
"""