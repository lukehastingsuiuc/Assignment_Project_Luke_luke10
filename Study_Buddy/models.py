from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

class Assignment(models.Model):
    asn_id = models.AutoField(primary_key=True)
    due_date = models.DateField()
    past_due = models.BooleanField(default=False)
    due_soon = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['due_date']

class Materials(models.Model):
    mat_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
