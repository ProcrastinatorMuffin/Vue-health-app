from fastapi import HTTPException
from models.Medication import Medication
from models.Patient import Patient
from models.MedicalRecord import MedicalRecord
import schema

def get_all():
    medications = Medication.all()
    return medications.all()
def add(medication_data: schema.MedicationBase):
    patient = Patient.find(medication_data.patient_id)
    if not patient:
        raise HTTPException(status_code=400, detail="Patient not Found")
    medical_record = MedicalRecord.find(medication_data.medicalrecord_id)
    if not medical_record:
        raise HTTPException(status_code=400, detail="Medical Record not Found")
    medication = Medication()
    medication.name = medication_data.name
    medication.frequency = medication_data.frequency
    medication.dosage = medication_data.dosage
    medication.start_date = medication_data.start_date
    medication.end_date = medication_data.end_date
    medication.patient_id = medication_data.patient_id
    medication.medicalrecord_id = medication_data.medicalrecord_id
    medication.save()
    return medication
def get(medication_id: int):
    medication = Medication.find(medication_id)
    if not medication:
        raise HTTPException(status_code=400, detail="Medication not Found")
    return medication
def delete(medication_id: str):
    medication =  Medication.find(medication_id)
    if medication:
        medication.delete()
        return medication
    else:
        raise HTTPException(status_code=400, detail="Medication not Found")
def get_medication(patient_id):
    patient = Patient.find(patient_id)
    if not patient:
        raise HTTPException(status_code=400, detail="Patient not Found")
    return patient.medications.all()