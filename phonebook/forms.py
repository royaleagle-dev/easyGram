from django import forms

class QuickAddForm(forms.Form):
    firstname = forms.CharField(label = 'Firstname', max_length = 255)
    lastname = forms.CharField(label = 'Lastname', max_length = 255)
    phone = forms.CharField(label = 'Phone Number', max_length = 255)
    email = forms.EmailField(label = 'Email Address', required=False)