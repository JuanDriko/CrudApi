from rest_framework import viewsets
from .models import Homework
from .serializer import HomeworkSerializer

# Create your views here.

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer