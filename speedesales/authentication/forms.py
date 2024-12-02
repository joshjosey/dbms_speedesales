from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''


        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class="form-text text-muted"><small>Your password must contain at least 8 characters, one letter, and cannot be too simple.'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password</small></span>'
        
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = ''
        
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = ''

class UpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = 'User Name'
        self.fields['username'].help_text = ''

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = 'Email'
        self.fields['email'].help_text = ''

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = 'First Name'
        
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = 'Last Name'


class UpdateCustomerForm(forms.ModelForm):
    phone = forms.CharField(label="Phone", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),required=False)
    address = forms.CharField(label="Address", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}), required=False)
    city = forms.CharField(label="City", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}), required=False)
    state = forms.CharField(label="State", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'State'}), required=False)
    zip = forms.CharField(label="Zip", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Zip'}), required=False)
    country = forms.CharField(label="Country", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}), required=False)

    class Meta:
        model = Customer
        fields = ('phone','address','city','state','zip','country')

    def __init__(self, *args, **kwargs):
        super(UpdateCustomerForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['phone'].label = 'Phone'