from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('view-set', views.HelloAPIViewset, base_name='view-set') 
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
	path('hello-view/',views.HelloAPIView.as_view()),
	path('',include(router.urls)),
]
