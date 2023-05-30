from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import list_app
from .serializers import list_appSerializer

class list_appViewSet(viewsets.ModelViewSet):
    queryset = list_app.objects.all()
    serializer_class = list_appSerializer

def listfunc(request):
    object_list = list_app.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def searchfunc(request):
    object_list = list_app.objects.all()
    return render(request, 'search_apex.html', {'object_list':object_list})


class listapiview(RetrieveAPIView):
    queryset = list_app.objects.all()
    serializer_class = list_appSerializer
    Permission_classes = [IsAuthenticated]



# Create your views here.
