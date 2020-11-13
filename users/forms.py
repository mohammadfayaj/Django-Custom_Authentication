from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from PIL import Image
from django.core.files import File
from users.models import Profile,Address
from intl_tel_input.widgets import IntlTelInputWidget
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class AddressForm(forms.ModelForm):                      
    class Meta:
        model = Address
        fields = ('first_name', 'last_name', 'phone_number' , 'house_number', 'division', 'city', 'zone', 'effective_delivery' )
        widgets = {
           
           'phone_number' :PhoneNumberPrefixWidget(attrs=
                {'placeholder': (u'Phone Number'),'id':'tel' ,'class': "form-control", 'label':(u'Cellphone number')}),
    }

class ProfileUpdateForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Profile
        fields = ('file', 'x', 'y', 'width', 'height', )
        widgets = {
            'file': forms.FileInput(attrs={
                'accept': 'image/*'  # this is not an actual validation! don't rely on that!
            })
        }

    def save(self):
        photo = super(ProfileUpdateForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
        resized_image.save(photo.file.path)

        return photo


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(label='Enter Username', help_text='* Username should not have any space' , min_length=4, max_length=150)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(label='Enter Username', help_text='* Username should not have any space' , min_length=4, max_length=150)
    class Meta:
        model = User
        fields = ['username', 'email',]
