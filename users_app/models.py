from django.db import models
    
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=45)
    age = models.IntegerField()
    belt = models.CharField(max_length=45,default='SOME STRING')
    academy_name = models.CharField(max_length=45,default='SOME STRING')



