from django.db import models

# Member Model
class Member(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensuring that emails are unique
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    yob = models.DateField()  # Year of Birth

    def __str__(self):
        return self.fullname  # Use fullname instead of name

# Appointment Model
class Appointment(models.Model):
    name = models.CharField(max_length=100)  # Name of the person making the appointment
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.DateTimeField()  # Date and time of the appointment
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    message = models.TextField()  # Additional message from the person

    def __str__(self):
        return f"Appointment with {self.name} on {self.date}"  # Clearer string representation
# Contact Model
class Contactss(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title
