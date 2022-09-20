from django import forms

CHOICES = [('M', 'Male'), ('F', 'Female')]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    gender = forms.CharField(label='gender', widget=forms.RadioSelect(choices=CHOICES))
    email = forms.EmailField(max_length=60)
    address = forms.CharField(max_length=100)
