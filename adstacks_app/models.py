from django.db import models

    

# Create your models here.

class AndroidApp(models.Model):
    app_name= models.CharField(max_length=100)
    version= models.CharField(max_length = 50)
    description=models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.app_name
