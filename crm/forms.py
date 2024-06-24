from django import forms
from .models import *
from django.forms import FileField, Form

class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('full_name', 'biz_name', 'address', 'email', 'phone', 'category')

    def __init__(self, *args, **kwargs):
        super(AddRecordForm, self).__init__(*args, **kwargs)

        self.fields['full_name'].label = 'Full name'
        self.fields['full_name'].widget.attrs['class'] = 'form-control'
        self.fields['full_name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['full_name'].help_text = ''

        self.fields['biz_name'].label = 'Business name'
        self.fields['biz_name'].widget.attrs['class'] = 'form-control'
        self.fields['biz_name'].widget.attrs['placeholder'] = 'Business Name'
        self.fields['biz_name'].help_text = ''

        self.fields['address'].label = 'Address'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = 'Address'
        self.fields['address'].help_text = ''

        self.fields['email'].label = 'Email'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].help_text = ''

        self.fields['phone'].label = 'Phone'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['phone'].help_text = ''

        self.fields['category'].label = 'Category'
        self.fields['category'].widget.attrs['class'] = 'form-select'
        self.fields['category'].widget.attrs['placeholder'] = 'Category'
        self.fields['category'].help_text = ''
   

class UploadForm(Form):
    records_file = FileField()

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)

        self.fields['records_file'].label = 'Accepts csv file only'
        self.fields['records_file'].widget.attrs['class'] = 'form-control'
        self.fields['records_file'].widget.attrs['placeholder'] = ''
        self.fields['records_file'].help_text = ''

class DateInput(forms.DateInput):
    input_type = 'date'

class AddTodoForm(forms.ModelForm):
    # due_date = forms.DateField(widget = forms.SelectDateWidget())

    class Meta:
        model = Todos
        fields = ('todos', 'due_date',)
        widgets = {
            'due_date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(AddTodoForm, self).__init__(*args, **kwargs)

        self.fields['todos'].label = ''
        self.fields['todos'].widget.attrs['class'] = 'form-control'
        self.fields['todos'].widget.attrs['placeholder'] = 'Task'
        self.fields['todos'].help_text = ''

class AddInteractions(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ('interaction_type', 'notes', 'follow_up', )
        # widgets = {
        #     'due_date': DateInput()
        # }

    def __init__(self, *args, **kwargs):
        super(AddInteractions, self).__init__(*args, **kwargs)

        self.fields['interaction_type'].label = ''
        self.fields['interaction_type'].widget.attrs['class'] = 'form-select'
        self.fields['interaction_type'].widget.attrs['placeholder'] = 'Notes'
        self.fields['interaction_type'].help_text = ''

        self.fields['notes'].label = ''
        self.fields['notes'].widget.attrs['class'] = 'form-control'
        self.fields['notes'].widget.attrs['placeholder'] = 'Notes'
        self.fields['notes'].help_text = ''

        self.fields['follow_up'].label = ''
        self.fields['follow_up'].widget.attrs['class'] = 'form-control'
        self.fields['follow_up'].widget.attrs['placeholder'] = 'Follow up actions'
        self.fields['follow_up'].help_text = ''

class AddTransaction(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('service', 'amount',)

    def __init__(self, *args, **kwargs):
        super(AddTransaction, self).__init__(*args, **kwargs)

        self.fields['service'].label = ''
        self.fields['service'].widget.attrs['class'] = 'form-control'
        self.fields['service'].widget.attrs['placeholder'] = 'Service rendered'
        self.fields['service'].help_text = ''

        self.fields['amount'].label = ''
        self.fields['amount'].widget.attrs['class'] = 'form-control'
        self.fields['amount'].widget.attrs['placeholder'] = 'Amount owed'
        self.fields['amount'].help_text = ''