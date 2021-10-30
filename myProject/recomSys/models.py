from django.db import models

# Create your models here.

class testMysql ( models.Model ) :

    testMysql = models.CharField ( 'testMysql' , max_length= 30 )
