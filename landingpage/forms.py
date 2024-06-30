from django import forms
from .models import Lead
from django.forms import FileField, Form

class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('full_name', 'email', 'location', )

    def __init__(self, *args, **kwargs):
        super(AddLeadForm, self).__init__(*args, **kwargs)

        self.fields['full_name'].label = 'Full name'
        self.fields['full_name'].widget.attrs['class'] = 'form-control'
        self.fields['full_name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['full_name'].help_text = ''

        self.fields['email'].label = 'Email'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].help_text = ''

        self.fields['location'].label = 'Location'
        self.fields['location'].widget.attrs['class'] = 'form-control'
        self.fields['location'].widget.attrs['placeholder'] = 'Location'
        self.fields['location'].help_text = ''

