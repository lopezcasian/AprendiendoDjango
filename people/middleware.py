from django.http import Http404
import random

class SecretMiddleware:

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self,request):
		# Antes de la vista 
		if not request.GET.get('secret'):
			raise Http404()
		if request.GET.get('secret') != 'platzi':
			raise Http404()


		response = self.get_response(request)
		# Despues de la vista
		return response

class ABMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self,request):
		# Antes de la vista 

		
		request.session['testab'] = random.choice(['a', 'b'])

		response = self.get_response(request)
		# Despues de la vista
		return response