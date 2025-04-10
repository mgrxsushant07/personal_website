from django.db import models

# Create your models here.

class candidate(models.Model):
    Full_Name = models.CharField(max_length=100)
    Date_of_Birth = models.DateField()
    CV = models.FileField(upload_to='cv/')
    Cover_Letter = models.FileField(upload_to='cover_letters/')
    Remark = models.TextField()

    def __str__(self):  
        return self.Full_Name
