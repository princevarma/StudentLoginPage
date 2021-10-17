from django.db import models

# Create your models here.
# and storing in database act as a mysql.

class Contact(models.Model):
    usn=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50,default="")
    sem=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.name


