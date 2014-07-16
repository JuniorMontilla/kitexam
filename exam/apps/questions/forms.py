from django import forms
from PIL import Image
from django.contrib.auth.models import  User
from django.utils.translation import ugettext as gettext

class registerform(forms.Form):
	first_name = forms.CharField(label="Nombres", widget=forms.TextInput())	
	last_name = forms.CharField(label="Apellidos",widget=forms.TextInput())
	nickname =  forms.CharField(label="Nickname",widget=forms.TextInput())	
	email = forms.EmailField(label="Email",widget=forms.TextInput())
	password = forms.CharField(label="Clave",widget=forms.PasswordInput(render_value=False ))	
	confirmpassword = forms.CharField(label="Confirmar Clave",widget=forms.PasswordInput(render_value=False ))	

	def clean_nickname(self):
		nickname = self.cleaned_data['nickname']
		try:
			u = User.objects.get(username=nickname)
		except User.DoesNotExist:
			return nickname
		raise forms.ValidationError('El nickname {0} ya existe'.format(nickname))

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('El email {0} ya esta registrado '.format(email))

	def clean_confirmpassword(self):
		password = self.cleaned_data['password']
		confirmpassword  = self.cleaned_data['confirmpassword']
		if password == confirmpassword:
			pass
		else:
			raise forms.ValidationError('Las claves  no coinciden')

class profileform(forms.Form):
	CHOICES=[('Python','Python'),('Linux','GNU/Linux')]
	avatar = forms.ImageField()
	selection = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

	def clean_avatar(self):
		avatar = self.cleaned_data.get('avatar', False)
		avatarimage = Image.open(avatar)
		if  avatar:
			w, h = avatarimage.size 
			#validate dimesions
			maxwidth = maxheight = 200
			if w > maxwidth  or h > maxheight:
				raise forms.ValidationError(gettext('El ancho y alto maximo soportado son 200px  200px'))
			#validate contenttype
			main, sub = avatar.content_type.split('/')
			if not (main == 'image' and sub.lower() in ['jpg','png','jpeg']):
				raise forms.ValidationError(gettext('Solo permitimos formatos jpg, png y jpeg'))
		else:
			raise ValidationError(gettext('upss no se ha podido leer la imagen'))
		return avatar
 
class  loginform(forms.Form):
	username = forms.CharField(label="Nick",widget=forms.TextInput())
	password = forms.CharField(label="Clave",widget=forms.PasswordInput(render_value=False))
