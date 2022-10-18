from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    sub_title=models.CharField(max_length=300,null=True)
    body=models.TextField()
    img=models.FileField(upload_to='news/%Y/%m/%d')
    avtor=models.ForeignKey(User,on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    views=models.IntegerField(default='0')

    def __str__(self):
        return self.title

class Odam(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.IntegerField(default='998901234567')

    class Meta:
        verbose_name_plural = 'Odam'

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(default='example@gmail.com')
    text = models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# class ContactResponse(models.Model):
#     email=models.ForeignKey(Contact.email,on_delete=models.CASCADE)
#     ism=models.ForeignKey(Contact.name,on_delete=models.CASCADE)
#     response=models.TextField()

class Kor(models.Model):
    son=models.IntegerField(default='1000000')