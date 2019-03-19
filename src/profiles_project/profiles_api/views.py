from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import request
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework import filters

from . import models
from . import serializers
from . import permissions

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
	
	serializer_class = serializers.HelloSerializer

	
	def list(self, request):
		
		a_viewset = [
			'It gives more functionality with less code. ',
			'It uses actions (LIST, RETRIEVE, CREATE, UPDATE, PARTIAL-UPDATE)',
		]
		
		return Response({'message': 'Hello!', 'a_viewset': a_viewset})
		
		
	def create(self, request):
		
		''' create a new hello message '''
		
		serializer = serializers.HelloSerializer(data = request.data)
		
		if serializer.is_valid():
			
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message': message})
		
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
		
	
	def retrieve(self, request, pk = None):
	
		''' Handles an object retrieval by id. '''
		
		return Response({'http_method': 'GET'})
		
		
	def update(self, request, pk = None):
		
		''' Handles updating an object '''
		
		return Response({'http_method': 'PUT'})
		
		
	def partial_update(self, request, pk = None):
	
		''' Handles partial updating an element.'''
		
		return Response({'http_method': 'PATCH'})
		
	def destroy(self, request, pk = None):
	
		''' Handles deleting an object. '''
		
		return Response({'http_method': 'DELETE'})
	
	

class UserProfileViewSet(viewsets.ModelViewSet):
	"""Handles creating, reading and updating profiles."""

	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,)
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'email',)
		
		
		
		
		