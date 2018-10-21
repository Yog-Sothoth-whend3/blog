from django.db import models

# Create your models here.

from datetime import *

class article_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(ISdelete = False )
    def create_article(self,tte,ctt,em):
        atc = self.model()
        atc.title = tte
        atc.context = ctt
        atc.date = datetime.now()
        atc.aemail = em
        atc.save()


    

class user_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(ISdelete = False )
    def create_user(self,name,mail,pw):
        uname = self.model()
        uname.username = name
        uname.email = mail
        uname.password = pw
        uname.save()        

    def users_aticle(self,all,one):
        return all.filter(aemail = one)





class user(models.Model):
    users = user_manager()
    objects = models.Manager()
    username = models.CharField(max_length = 18)
    email = models.EmailField(primary_key = True)
    password = models.CharField(max_length = 64)
    ISdelete = models.BooleanField(default = False)




class article(models.Model):
    articles = article_manager()    
    objects = models.Manager()
    title = models.CharField(max_length = 39)
    context = models.TextField()
    date = models.DateTimeField()
    aemail = models.ForeignKey(user,on_delete=models.CASCADE)
    ISdelete = models.BooleanField(default = False)
    





    
