from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# class is a special keyword that indicates that we are defining an object.
# Post is the name of our model. We can give it a different name (but we must avoid special characters and whitespace).
# Always start a class name with an uppercase letter.
# models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database


class Ccode(models.Model):
	#models.ForeignKey – this is a link to another model.
	text = models.TextField()
