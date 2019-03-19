from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import request
from rest_framework import status
from . import serializers

from rest_framework import viewsets

# Create your views here.
class HelloAPIView(APIView):

	''' Test API view.'''
	
	serializer_class = serializers.HelloSerializer
	
	def get(request, self, format=None):
	
		''' Returns a list of API view features. '''
		
		an_apiview = [
			'Uses HTTP methods as functions(GET, POST, PUT, PATCH, DELETE).',
			'It is similar to a traditional Django View',
			'Gives you the most control over your logic',
			'Is mapped manually to URLs',
		]
		
		return Response({'message': "Hello World", 'an_apiview': an_apiview})

	def post(self, request):
		
		''' Create a hello message with our name. '''
		#print(request.data)
		serializer = serializers.HelloSerializer(data = request.data)
		
		if serializer.is_valid():
			#print(serializer.data)
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message': message})
		
		else:
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
			

class HelloAPIViewset(viewsets.ViewSet):

	''' Test Api Viewset. '''
	
	def list(self, request):
		a_viewset = [
			'It gives more functionality with less code. ',
			'It uses actions (LIST, RETRIEVE, CREATE, UPDATE, PARTIAL-UPDATE)',
		]
		
		return Response({'message': 'Hello!', 'a_viewset': a_viewset})
		