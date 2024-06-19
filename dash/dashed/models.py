from django.db import models

class MemberDetail(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    payer = models.CharField(max_length=255)
    membership_number = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    validity = models.CharField(max_length=255)
    scheme = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.membership_number})"

class Discharge(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    payer = models.CharField(max_length=255)
    membership_number = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    validity = models.CharField(max_length=255)
    scheme = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.membership_number})"

class Discharged(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    payer = models.CharField(max_length=255)
    membership_number = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    validity = models.CharField(max_length=255)
    scheme = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.membership_number})"


# Create your models here.
