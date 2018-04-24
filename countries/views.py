from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
class HomeView(TemplateView):
	template_name = "countries/home.html"


class TagsView(TemplateView):
	template_name = "countries/tags.html"


class CountryDetailView(TemplateView):
	template_name = "countries/country_detail.html"


	def get_context_data(self, *args, **kwargs):
		code = kwargs['code']
		return {'code':code}

class CountryDetailIDView(TemplateView):
	template_name = "countries/country_id_detail.html"


	def get_context_data(self, *args, **kwargs):
		code_id = kwargs['id']
		return {'id':code_id}