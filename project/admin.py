from django.contrib import admin
from .models import Nurse, Patient, Hospital, Diagnosis, Ward, HealthRecording


admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Diagnosis)
admin.site.register(Hospital)
admin.site.register(Ward)
admin.site.register(HealthRecording)