from django.db import models
from django.contrib.auth.models import User as DjangoUser
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from datetime import date

userTypes = ( ('admin','admin'),('dda','dda'), ('ado', 'ado') )

class User(models.Model):
    name = models.CharField(max_length = 100, blank = False, null = False, unique = False)
    typeOfUser = models.CharField(max_length=10,choices=userTypes,default='intern')
    auth_user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    
    def __str__(self):
        if self.name:
            return str(self.name)
        else:
            return self.auth_user.username
    class Meta:
        ordering = ["name"]