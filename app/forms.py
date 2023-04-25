from django import forms
from django.core import validators

def check_for_q(value):
    if value[0].upper()=='Q':
        raise forms.ValidationError('Does not startswith q')
def check_for_len(v):
    if len(v)<5:
        raise forms.ValidationError('Length must be greater than 5')

class NameForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_q,validators.MaxLengthValidator(5)])
    fathername=forms.CharField(max_length=100,validators=[check_for_len])
    email=forms.EmailField()
    reemail=forms.EmailField()
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot Catched')
    def clean(self):
        em=self.cleaned_data['email']
        reem=self.cleaned_data['reemail']
        if em!=reem:
            raise forms.ValidationError('Emails are Mismatching')