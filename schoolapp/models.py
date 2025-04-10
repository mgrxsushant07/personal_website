from django.db import models

class Student(models.Model):
    photo = models.ImageField(upload_to='student_images/')
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(default='hello@gmail.com')
    address = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=100,default='Maths')
    message = models.TextField(default='sample')

    def __str__(self):
        return self.name
