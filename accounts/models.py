from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    """
    Here CustomUser is the subclasss of AbstractUser which makes the default permission and extent as per as our requeriment.
    """
    pass

