from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloAPIView(APIView):

	''' Test API view.'''
	
	def get(request, self, format=None):
	
		''' Returns a list of API view features. '''
		
		an_apiview = [
			'Uses HTTP methods as functions(GET, POST, PUT, PATCH, DELETE).',
			'It is similar to a traditional Django View',
			'Gives you the most control over your logic',
			'Is mapped manually to URLs',
		]
		
		return Response({'message': "Hello World", 'an_apiview': an_apiview})