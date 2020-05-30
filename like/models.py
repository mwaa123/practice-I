from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 
class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()
    img= models.ImageField(default="default.jpg",upload_to='gala/')
    name = models.TextField( blank=True)

      
    def __str__(self):
        return f'{self.user.username} Profile'



class Image(models.Model):
    name = models.TextField()
    caption = models.TextField()
    img= models.ImageField(upload_to='gala/',blank=True)
    comments = models.TextField()
    prof= models.ForeignKey('Profile',on_delete=models.CASCADE ,null=True )

    def __str__(self):
        return f'{self.user.username}name'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          