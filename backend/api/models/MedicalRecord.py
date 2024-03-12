""" MedicalRecord Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_many
class MedicalRecord(Model):
    """MedicalRecord Model"""
    @has_many("id", "medicalrecord_id")
    def medications(self):
        from .Medication import Medication
        return Medication