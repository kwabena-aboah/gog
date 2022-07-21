from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, generics
from yaml import serialize
from . models import User
from .serializer import UserSerializer, MyTokenObtainPairSerializer, LogoutSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission, AllowAny, IsAuthenticated, IsAdminUser, SAFE_METHODS
from rest_framework_simplejwt.views import TokenObtainPairView


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = MyTokenObtainPairSerializer


class Logout(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated|ReadOnly,)

    def post(self, request):
        #simply delete the token to force a login
        # request.user.auth_token.delete()
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)