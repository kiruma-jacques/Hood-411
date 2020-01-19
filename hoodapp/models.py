from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avi=ImageField(null=True)
    bio=models.CharField(max_length=240)
    hood=models.CharField(max_length=240, null=True)

class Hood(models.Model):
    photo=ImageField(null=True)
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    occupants_count=models.IntegerField(default=0)
    group_member=models.ManyToManyField(User, through='Member')
    police_contact=models.IntegerField()
    hospital_contact=models.IntegerField()

    def __str__(self):
        return self.name

    @classmethod
    def single_hood(cls, id):
        return cls.objects.get(id)

class Biz(models.Model):
    hood=models.ForeignKey(Hood, related_name='Biz')
    name=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.name

class Member(models.Model):
    hood=models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='member')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='member')

    def __str__(self):
        return self.user.username

class Posts(models.Model):
    hood=models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='Post')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='Post')
    post=models.TextField()

    def __str__(self):
        return self.post
