from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstituteViewSet, CourseViewSet, StudentViewSet, ProfileViewSet, search

router = DefaultRouter()
router.register(r'institutes', InstituteViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', search, name='search'),
    ]

