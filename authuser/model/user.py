from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):

    name = models.CharField(max_length=255, db_column="NAME")

    username = models.CharField(max_length=255, unique=True, db_column="USERNAME")

    email = models.EmailField(blank=True, db_column="EMAIL")

    password = models.CharField(max_length=255, db_column="PASSWORD")

    address = models.CharField(max_length=255, db_column="ADDRESS")

    designation = models.CharField(max_length=255, db_column="DESIGNATION")

    is_full_time = models.BooleanField(default=True, db_column="FULLTIME")
    contact = models.CharField(
        max_length=255, blank=True, null=True, unique=True, db_column="CONTACT"
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        db_table = "USER"
