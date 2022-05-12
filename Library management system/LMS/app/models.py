from django.db import models

# Create your models here.
class Books(models.Model):
    book_name=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    is_issued=models.BooleanField()
    book_type=models.CharField(max_length=30)