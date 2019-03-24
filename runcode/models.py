from django.conf import settings
from django.db import models
#from django.conf import settings
from django.utils import timezone

# Create your models here.

# class is a special keyword that indicates that we are defining an object.
# Post is the name of our model. We can give it a different name (but we must avoid special characters and whitespace).
# Always start a class name with an uppercase letter.
# models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database


'''def user_directory_path(instance, filename):
	# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
	filename = timezone.now().strftime('%d-%m-%y_%H:%M:%S.py')
	return 'data/user_{0}/{1}'.format(instance.user.id, filename)'''



class Pycode(models.Model):
    # models.ForeignKey – this is a link to another model.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    postdate = models.DateTimeField('time saved')
    pycode = models.FileField()
    result_output = models.TextField(default='No Output')
    result_error = models.TextField(default='No Error')

    #submitted_by = models.ForeignKey(usermod.User, on_delete=models.CASCADE)
