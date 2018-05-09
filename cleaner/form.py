from django import forms


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class edit(forms.Form):
    dummy = forms.DecimalField(label='Enter the column number for Dummy Variable Introduction',
                               widget=forms.NumberInput(attrs={'multiple': True}))


class delc(forms.Form):
    delc1 = forms.DecimalField(label='Enter the column number for deleting',
                               widget=forms.NumberInput(attrs={'multiple': True}))
