from django import forms

class ContactForm(forms.Form):
    category = forms.CharField()
    subject = forms.CharField()
    message = forms.CharField()