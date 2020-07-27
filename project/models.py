from django.db import models
from datetime import datetime


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=50)

    def __str__(self):
        return self.hospital_name


class Ward(models.Model):
    ward_name = models.CharField(max_length=50)
    ward_tel_num = models.IntegerField()
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name="wards")

    def __str__(self):
        return self.ward_name


class Nurse(models.Model):
    full_name = models.CharField(max_length=50)
    ward = models.ForeignKey(
        Ward, on_delete=models.CASCADE, related_name="nurses")

    def __str__(self):
        return self.full_name


class Patient(models.Model):
    full_name = models.CharField(max_length=50)
    nhs_number = models.IntegerField()
    sex = models.CharField(max_length=1)
    status = models.BooleanField(default=True)
    dob = models.DateField(max_length=8)

    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class HealthRecording(models.Model):
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    oxygen_therapy = models.BooleanField(default=False)
    heart_rate = models.IntegerField()
    date_modified = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="health_recordings")

    CONDITIONS = (
        ("Stable", "Stable"),
        ("Unstable", "Unstable"),
        ("Critical", "Critical"),
    )

    condition = models.CharField(
        max_length=10,
        choices=CONDITIONS,
        blank=True,
        default="Stable",
    )

    class Meta:
        ordering = ['-date_modified']

    def __str__(self):
        return f"Health Recording: {self.patient.full_name}"


class Diagnosis(models.Model):
    diagnosis_name = models.CharField(max_length=50)
    treatment = models.CharField(max_length=150, null=True)
    date_diagnosed = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="diagnoses")

    SEVERITY = (
        ("Mild", "Mild"),
        ("Moderate", "Moderate"),
        ("Severe", "Severe"),
    )

    severity = models.CharField(
        max_length=10,
        choices=SEVERITY,
        blank=True,
        default="Mild",
    )

    def __str__(self):
        return self.diagnosis_name
