from rest_framework import serializers
from .models import Nurse, Patient, Hospital, Diagnosis, Ward, HealthRecording


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ["full_name"]


class HealthRecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecording
        fields = ["temperature", "oxygen_therapy", "heart_rate",
                  "condition", "date_modified"]


class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ["diagnosis_name", "treatment",
                  "date_diagnosed", "severity"]


class WardSerializer(serializers.ModelSerializer):
    # Get reverse relationship
    nurses = NurseSerializer(read_only=True, many=True)

    class Meta:
        model = Ward
        fields = ["ward_name", "ward_tel_num", "nurses"]


class PatientSerializer(serializers.ModelSerializer):
    # Get reverse relationships
    health_recordings = HealthRecordingSerializer(read_only=True, many=True)
    diagnoses = DiagnosisSerializer(read_only=True, many=True)
    ward = WardSerializer(many=False)

    class Meta:
        model = Patient
        fields = ["full_name", "nhs_number", "status", "ward",
                  "sex", "dob", "health_recordings", "diagnoses"]


class HospitalSerializer(serializers.ModelSerializer):
    # Get reverse relationship
    wards = WardSerializer(read_only=True, many=True)

    class Meta:
        model = Hospital
        fields = ["hospital_name", "wards"]
