from django import forms
from people.models import Person
from django.forms import ModelForm
from countries.models import Country

class RegisterForm(forms.Form):
	first_name = forms.CharField(label='first name')
	nacionality = forms.ModelMultipleChoiceField(queryset=Country.objects.all())
	father = forms.ModelChoiceField(required=False, queryset=Person.objects.all())

class RegisterFormModel(forms.ModelForm):

	def __init__(self, fathers, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['father'].queryset = fathers

	class Meta:
		model = Person
		fields = ['first_name', 'nacionality', 'father']
