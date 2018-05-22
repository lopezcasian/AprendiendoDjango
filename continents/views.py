from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from continents.models import Continent
# Create your views here.
class ContinentsView(ListView):
	template_name = 'continents/continents.html'
	model = Continent

	"""def get_context_data(self, *args, **kwargs):
		america = {'name':'américa', 'translation':'america', 'color':'#000000'}
		antartida = {'name':'antártida', 'translation':'antarctica', 'color':'#FFFF00'}
		europa = {'name':'europa', 'translation':'europe', 'color':'#F1D142'}
		africa = {'name':'africa', 'translation':'africa', 'color':'#F04261'}
		asia = {'name':'asia', 'translation':'asia', 'color':'#EE65EE'}
		oceania = {'name':'oceania', 'translation':'oceania', 'color':'#EE65DD'}

		continents = [
			america,
			africa,
			asia,
			oceania,
			antartida
		]

		return {'continents':continents}"""