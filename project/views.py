# 1 Django core
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist

# 2 Rest framework
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound  # Equivalent to Django's 404
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

# 3 Project
from .models import Patient
from .serializers import PatientSerializer


@api_view(["GET"])
def patients(request):
    """ 
    Retrieves all Patient objects in JSON. 
    """
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def patients_detail(request, nhs_number):
    """ 
    Retrieves a single Patient object by nhs_number in JSON. 
    """
    try:
        patient = Patient.objects.get(nhs_number=nhs_number)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        raise NotFound(
            detail="Patient with NHS number of {nhs_number} does not exist!", code="404")
