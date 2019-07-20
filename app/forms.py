from django import forms


class NewForm(forms.Form):
    text = forms.CharField(max_length=1000)
    choice = forms.CharField(widget=forms.RadioSelect(choices=[('char','charEncrypt'),('sym','symEncrypt')]))
