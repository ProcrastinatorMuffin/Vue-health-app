""" Patient Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_many

class Patient(Model):
    """Patient Model"""
    @has_many("id", "patient_id")
    def medicalrecords(self):
        from .MedicalRecord import MedicalRecord
        return MedicalRecord
    
    @has_many("id", "patient_id")
    def appointments(self):
        from .Appointment import Appointment
        return Appointment