from django.db import models

# Create your models here.
class Portfolio(models.Model):
    port_name = models.CharField(max_length = 300)
    port_type = models.CharField(max_length = 30)
    image = models.ImageField()


    def __str__(self):
        return self.port_name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        
        return url
    

class Contact(models.Model):
    name = models.TextField()
    email= models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name