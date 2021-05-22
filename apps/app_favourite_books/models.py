from django.db import models
from apps.app_login_register.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="Sin descripción")
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete = models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)