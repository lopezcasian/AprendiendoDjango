from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic import TemplateView
from countries.models import Country
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from countries.forms import CountryCreateFormModel

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

class CountryDetailIDView(DetailView):
	template_name = "countries/country_id_detail.html"

	model = Country

	"""def get_context_data(self, *args, **kwargs):
		country = get_object_or_404(Country, id=kwargs['id'])

		return {'country':country}"""

class CountrySearchView(ListView):
	template_name = 'countries/search.html'
	model = Country

	def get_queryset(self):
		query = self.kwargs['query']
		return Country.objects.filter(name__contains=query)


class CreateCountryView(TemplateView):
	template_name = "countries/register.html"

	def dispatch(self, request, *args, **kwargs):
		self.form = CountryCreateFormModel(request.POST or None)
		return super().dispatch(request, *args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		return {'form': self.form}

	def post(self, request, *args, **kwargs):	

		if self.form.is_valid():
			country = self.form.save()

			return JsonResponse({ "name":country.name })

		return self.get(request, *args, **kwargs)
