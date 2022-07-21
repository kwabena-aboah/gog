from django.contrib.auth.models import User
from rest_framework import viewsets
from . models import District, Region, NationalReport
from .serializer import DistrictSerializer, RegionSerializer, NationalReportSerializer
from users.permissions import SafeMethodsOnly, AdminOrAuthorCanEdit
from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.views import TokenObtainPairView


class DistrictViewset(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    # permission_classes = [IsAuthenticated]
    
class RegionViewset(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

# class PublicAuthorityViewset(viewsets.ModelViewSet):
#     queryset = PublicAuthority.objects.all()
#     serializer_class = PublicAuthoritySerializer
#     # permission_classes = [IsAuthenticated]


class NationalReportViewset(viewsets.ModelViewSet):
    queryset = NationalReport.objects.all()
    serializer_class = NationalReportSerializer
    permission_classes = [SafeMethodsOnly, IsAuthenticated]