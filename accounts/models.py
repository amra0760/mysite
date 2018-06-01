from django.db import models
# from django.urls import reverse

# Create your models here.
class Website(models.Model):
    site_name = models.CharField(max_length = 1000)
    
    def get_absolute_url(self):
        # return reverse('accounts:detail',kwargs={'pk':self.pk})
        # return reverse('accounts:index')
        return u'/accounts/%d' % self.id 
    
    def __str__(self):
        return self.site_name
        

class Email(models.Model):
    email = models.CharField(max_length = 1000, default="johndoe@example.com")
    password = models.CharField(max_length = 1000, default="password123")
    # votes = models.IntegerField(default = 0)
    website = models.ForeignKey(Website, on_delete=models.CASCADE) #makes sure that each choice is linked to the correct question and deletes it if the question is deleted
    
    def __str__(self):
        return self.email + " - " + self.password