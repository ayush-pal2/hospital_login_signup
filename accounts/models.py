from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"
