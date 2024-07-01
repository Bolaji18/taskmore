from django.db import models
from django.contrib.auth.models import User

class info(models.Model):
    title = models.CharField(max_length=800, null=True, verbose_name="Title")
    description = models.TextField(max_length=80, null=True, verbose_name="description")
    statuses = [
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Overdue', 'Overdue'),
    ]
    status = models.CharField(max_length=20, choices=statuses, verbose_name="status")
    priorities = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    priority = models.CharField(max_length=20, choices=priorities, verbose_name="Priority")
    due_date = models.DateTimeField(verbose_name="Due date")
    category = models.CharField(max_length=800, null=True, verbose_name="Category")
    assigned_to =  models.ForeignKey(User, on_delete=models.CASCADE)
