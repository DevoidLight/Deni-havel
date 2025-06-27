from django.db import models
from django.contrib.auth.models import User

class BusinessIdea(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ideas')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    required_investment = models.DecimalField(max_digits=10, decimal_places=2)
    business_plan = models.FileField(upload_to='business_plans/', null=True, blank=True)

# Create your models here.
