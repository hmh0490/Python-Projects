# models for the database
from django.db import models

# design the database
class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    # if we create a class and then print it out, it will give us a string,
    # and not an object such as <__main__.Foo object at 0x000002707859F370>
    # this case: if we create admin interface, we will see the name there
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
