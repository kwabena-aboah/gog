from django.shortcuts import render
from . models import Region, District, NationalReport


def index(request):
    region = Region.objects.all()
    district = District.objects.all()
    # public_authority = PublicAuthority.objects.all()
    national_report = NationalReport.objects.all()
    context = {
        'region': region,
        'district': district,
        # 'public_authority': public_authority,
        'national_report': national_report
    }
    return render(request, 'report/index.html', context)