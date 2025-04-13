from django import forms


class LongUrlForms(forms.Form):
    url = forms.URLField()
