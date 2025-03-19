from django import forms
from .models import User
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'age', 'gender', 'address']

    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}),
        error_messages={'required': 'Name is required.'}
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        error_messages={'required': 'Email is required.', 'invalid': 'Enter a valid email address.'}
    )

    phone = forms.CharField(
        max_length=15,
        required=True,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit phone number.')],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
        error_messages={'required': 'Phone number is required.'}
    )

    age = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(0, 'Age cannot be negative.'), MaxValueValidator(120, 'Enter a realistic age.')],
        widget=forms.NumberInput(attrs={'placeholder': 'Enter your age'}),
        error_messages={'required': 'Age is required.'}
    )

    gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        required=True,
        widget=forms.Select(),
        error_messages={'required': 'Gender is required.'}
    )

    address = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Enter your address'}),
        error_messages={'required': 'Address is required.'}
    )