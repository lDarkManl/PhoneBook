from rest_framework import viewsets
from .models import Role
from .serializers import RoleSerializer, UserSerializer
from django.contrib.auth.models import User

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer





