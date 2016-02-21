from django import forms

class FormOrder(forms.Form):
	name = forms.CharField(required=True, max_length=100)
	email = forms.EmailField(required=True)