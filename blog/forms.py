from django import forms
from .models import Post
from .models import Ccode

class PostForm(forms.ModelForm):
#PostForm is the name of the form
	class Meta:
		#Tell django which model should be used to create this form
		model = Post
		#Tell django which fields should be imported in the form
		fields = ('title', 'text',)


class CcodeForm(forms.ModelForm):
#PostForm is the name of the form
	class Meta:
		#Tell django which model should be used to create this form
		model = Ccode
		#Tell django which fields should be imported in the form
		fields = ('text',)
