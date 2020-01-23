from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avi=ImageField(null=True)
    bio=models.CharField(max_length=240)
    hood=models.CharField(max_length=240, null=True)

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

class Hood(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='hood', null=True, blank=True)
    photo=ImageField(null=True)
    name=models.CharField(max_length=200,null=True)
    location=models.CharField(max_length=200,null=True)
    occupants_count=models.IntegerField(default=0,null=True)
    police_contact=models.IntegerField(null=True)
    hospital_contact=models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def single_hood(cls, id):
        return cls.objects.get(id)

class Biz(models.Model):
    hood=models.ForeignKey(Hood, related_name='Biz', null=True)
    name=models.CharField(max_length=200, null=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.name

    def save_biz(self):
        self.save()

    @classmethod
    def search_by_name(cls, search_term):
        biz=cls.objects.filter(name__icontains=search_term)
        return biz

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

    def save_profile(self):
        self.save()
