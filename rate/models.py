from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    image = CloudinaryField('image')
    bio = models.TextField(max_length=255)
    job_title = models.CharField(max_length=255)
    dateupdated= models.DateField(auto_now_add=True )

    def __str__(self):
        return self.user.username
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()  

    def update_bio(self,bio):
        self.bio = bio
        self.save()
    def update_job_title(self,job_title):
        self.job_title = job_title
        self.save()    
    def update_image(self,image):
        self.image = image
        self.save()        

