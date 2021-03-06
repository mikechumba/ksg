from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField,FileField

# Create your models here.
class Role(models.Model):

   role = models.CharField(max_length=50)

   @classmethod
   def get_role(cls,role):
      role = cls.objects.filter(role=role).first()
      return role

   def __str__(self):
      return self.role

class Profile(models.Model):

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   bio = models.TextField()
   avatar = ImageField()
   role = models.ForeignKey(Role, on_delete=models.CASCADE)

   @classmethod
   def create_profile(cls,user,role):
      profile = cls(user=user,bio='',avatar='889f3b4b-40f9-4306-9a26-a1eb7225790f/default.jpg',role=role)
      return profile

   def __str__(self):
      return f"{self.user.first_name} {self.user.last_name}"

class Post(models.Model):

   author = models.ForeignKey(Profile, on_delete=models.CASCADE)
   name = models.CharField(max_length=50)
   medium = models.CharField(max_length=50,null=True)
   logline = models.TextField(max_length=300)
   file = models.FileField(upload_to='screenplay', max_length=100)
   genre = models.CharField(max_length=50,null=True)

   def __str__(self):
      return self.name

   @classmethod
   def get_posts(cls,author):
      posts = cls.objects.filter(author=author)
      return posts

   @classmethod
   def by_medium(cls,medium):
      posts = cls.objects.filter(medium=medium)
      return posts

   @classmethod
   def by_category(cls,ctgry):
      posts = cls.objects.filter(category=ctgry)
      return posts

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


class Genres(models.Model):

   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name

   @classmethod
   def get_all(cls):
      genres = cls.objects.all()
      return genres

   class Meta:
      verbose_name_plural = 'Genres'