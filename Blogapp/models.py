from django.db import models

# Create your models here.


class Blogpost(models.Model):
    '''Creating a datastructure to accept user input'''
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''To return the needed values on the blogpage'''
        return self.title, self.date_time, self.id
