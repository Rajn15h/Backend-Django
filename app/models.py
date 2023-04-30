from django.db import models

# Create your models here.
class info(models.Model):
    Fname=models.CharField(max_length=20)
    Lname=models.CharField(max_length=20,null=True)
    Age=models.IntegerField(null=True)
    Bloodgroupchoices=[
        ('A+','A+'),
        ('B+','B+'),
        ('AB+','AB+'),
        ('O+','O+')
    ]
    Bloodgroup=models.CharField(choices=Bloodgroupchoices,null=True,max_length=10)

    def __str__(self):
        return self.Fname
        
