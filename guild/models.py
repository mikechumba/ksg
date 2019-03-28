from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField,FileField

# Create your models here.
class Role(models.Model):

   role = models.CharField(max_length=50)

   def __str__(self):
      return self.role

class Profile(models.Model):

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   bio = models.TextField()
   avatar = ImageField()
   role = models.ForeignKey(Role, on_delete=models.CASCADE)

   @classmethod
   def create_profile(cls,user,role):
      profile = cls(user=user,bio='',avatar='default.jpg',role=role)
      return profile

   def __str__(self):
      return f"{self.user.first_name} {self.user.last_name}"

class Post(models.Model):

   author = models.ForeignKey(Profile, on_delete=models.CASCADE)
   name = models.CharField(max_length=50)
   logline = models.TextField(max_length=140)
   file = FileField()

   def __str__(self):
      return self.name

class Review(models.Model):

   author = models.ForeignKey(Profile, on_delete=models.CASCADE)
   review = models.TextField()
   on = models.ForeignKey(Post, on_delete=models.CASCADE)

   def __str__(self):
      return f"{self.author.user.first_name} on {self.on.name}"

class Messages(models.Model):

   sender = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='sender')
   receiver = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='receiver')
   message = models.TextField(max_length=5)
   time_sent = models.DateField(auto_now=True)

   def __str__(self):
      return self.message

   class Meta:
      verbose_name_plural = 'Messages'
