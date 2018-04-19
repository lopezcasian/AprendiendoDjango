
def countries_data(request):
	colombia = {'nombre': 'colombia', 'codigo':'CO'}
	usa = {'nombre': 'estados unidos', 'codigo':'USA'}
	mexico = {'nombre':'mexico', 'codigo': 'MX'}

	countries = [colombia, usa, mexico]
	return {'countries':countries}