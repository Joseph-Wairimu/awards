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


class Project(models.Model):
    title = models.CharField(max_length=255)
    image = CloudinaryField('image')
    description = models.TextField(max_length=255)
    link =models.URLField(max_length=200)
    user = models.ForeignKey('auth.user',on_delete=models.CASCADE,related_name='user')
    dateupdated= models.DateField(auto_now_add=True )

    def __str__(self):
        return self.title
    def save_project(self):
        self.save()
    def delete_project(self):
        self.delete()
    

    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

RATE_CHOICES = [
(1,'1-Trash'),
(2,'2-Horrible'),
(3,'3-Terrible'),
(4,'4-Bad'),
(5,'5- ok'),
(6,'6-Well'),
(7,'7-Good'),
(8,'8-Very Good'),
(9,'9-Excellent'),
(10,'10-Perfect'),
]

class Rating(models.Model):
    design = models.IntegerField(choices = RATE_CHOICES,default=0)
    usability = models.IntegerField(choices = RATE_CHOICES,default=0)
    content = models.IntegerField(choices = RATE_CHOICES,default=0)
    developer=models.IntegerField(choices = RATE_CHOICES,default=0)
    creativity=models.IntegerField(choices = RATE_CHOICES,default=0)
    average = models.IntegerField(default=0 )
    review = models.TextField(max_length=2555,blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='project')
    user= models.ForeignKey(User,on_delete=models.CASCADE,related_name='project',null=True)
    dateupdated= models.DateField(auto_now_add=True )


    def __str__(self):
        return self.project.user.username
    def save_rating(self):
        self.save()
    def delete_rating(self):
        self.delete()        
    def average_rating(self):
        design = self.design
        usability = self.usability
        content = self.content
        developer = self.developer
        creativity = self.creativity
        average = (design + usability + content + developer + creativity)/5
        return average    