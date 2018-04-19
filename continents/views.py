from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class ContinentsView(TemplateView):
	template_name = 'continents/continents.html'

	def get_context_data(self, *args, **kwargs):
		america = {'nombre':'américa', 'traduccion':'america', 'color':'#000000'}
		antartida = {'nombre':'antártida', 'traduccion':'antarctica', 'color':'#FFFF00'}
		europa = {'nombre':'europa', 'traduccion':'europe', 'color':'#F1D142'}
		africa = {'nombre':'africa', 'traduccion':'africa', 'color':'#F04261'}
		asia = {'nombre':'asia', 'traduccion':'asia', 'color':'#EE65EE'}
		oceania = {'nombre':'oceania', 'traduccion':'oceania', 'color':'#EE65DD'}

		continents = [
			america,
			africa,
			asia,
			oceania,
			antartida
		]

		return {'continents':continents}