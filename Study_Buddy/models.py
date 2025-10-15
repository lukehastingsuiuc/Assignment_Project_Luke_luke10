from django.db import models
from django.urls import reverse

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    def __str__(self):
        base = f"{self.email}"
        return f"{base}"

    def get_absolute_url(self):
        return reverse('user-detail-url',
                       kwargs={'primary_key': self.pk}
                       )

class Assignment(models.Model):
    asn_id = models.AutoField(primary_key=True)
    due_date = models.DateField()
    past_due = models.BooleanField(default=False)
    due_soon = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments_related_name')
    class Meta:
        ordering = ['due_date']
        def __str__(self):
            base = f"{self.due_date}"
            return f"{base}"

class Materials(models.Model):
    mat_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='materials_related_name')
