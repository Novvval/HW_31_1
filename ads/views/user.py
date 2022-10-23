from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from ads.models import User
from ads.serializers import UserSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
