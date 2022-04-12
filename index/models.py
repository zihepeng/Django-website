from django.db import models

# Create your models here.
class grade(models.Model):
    gradetype = models.CharField(max_length=100,unique=True,null=False,verbose_name="grade type")
    isDelete = models.BooleanField(default=True)

    def __str__(self):
        return "grade(gradetype=%s)" % self.gradetype



class movies(models.Model):
    mname = models.CharField(max_length=100,unique=True,null=False, verbose_name="movie name")
    mduration = models.IntegerField(unique = False)
    mimg = models.CharField(max_length=100,unique=True,null=True, verbose_name="movie image")
    mticket = models.CharField(max_length=100,unique=True,null=True, verbose_name="movie ticket",default="")
    mgradetype = models.ForeignKey(grade,null=True,on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=True)


    def __str__(self):
        return "movies(mname=%s)" % self.mname