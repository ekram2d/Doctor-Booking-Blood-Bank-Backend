
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'doctor', views.DoctorOverview, basename='doctor')
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('', include(router.urls)),
]