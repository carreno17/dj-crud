from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class CreateTask(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    important = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return "User: {} , Title: {}".format(self.user, self.title)

