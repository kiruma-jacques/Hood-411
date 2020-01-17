from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Hood(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='Hood')
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    occupants_count=models.IntegerField(default=0)
    group_member=models.ManyToManyField(User, through='Member')
    police_contact=models.IntegerField()
    hospital_contact=models.IntegerField()

    def __str__(self):
        return self.name

class Biz(models.Model):
    neighbourhood=models.ForeignKey(Hood, related_name='Biz')
    name=models.CharField(max_length=200)
    description=models.TextField()
    category=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Member(models.Model):
    hood=models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='member')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='member')

    def __str__(self):
        return self.user.username
