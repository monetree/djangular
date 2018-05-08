from django.db import models

class Angular(models.Model):
    name   = models.CharField(max_length=60,null=True,blank=True,default="default name")
    number = models.IntegerField(null=True,blank=True,default=0000000000)

    def __str__(self):
        return self.name
