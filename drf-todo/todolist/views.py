from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from todolist.models import Todo
from todolist.serializers import TodoSerializer

# Create your views here.


class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["title", "description"]
    search_fields = ["title", "description"]


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
