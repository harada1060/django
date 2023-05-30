from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import list_appViewSet, listfunc, searchfunc


router = DefaultRouter()
router.register('list_app', list_appViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('list/', listfunc, name='list'),

    path('search_apex/', searchfunc, name='apex'),

]

