from fastapi import HTTPException
from models.MedicalRecord import MedicalRecord
from models.Patient import Patient
import schema

def get_all():
    medicalRecords = MedicalRecord.all()
    return medicalRecords.all()
def add(medicalRecord_data: schema.MedicalRecordBase):
    patient = Patient.find(medicalRecord_data.patient_id)
    if not patient:
        raise HTTPException(status_code=400, detail="Patient not Found")
    medicalRecord = MedicalRecord()
    medicalRecord.date = medicalRecord_data.date
    medicalRecord.diagnosis = medicalRecord_data.diagnosis
    medicalRecord.patient_id = medicalRecord_data.patient_id
    medicalRecord.save()
    return medicalRecord
def get(medicalRecord_id: int):
    medicalRecord = MedicalRecord.find(medicalRecord_id)
    if not medicalRecord:
        raise HTTPException(status_code=400, detail="MedicalRecord not Found")
    return medicalRecord
def delete(medicalRecord_id: str):
    medicalRecord =  MedicalRecord.find(medicalRecord_id)
    if medicalRecord:
        medicalRecord.delete()
        return medicalRecord
    else:
        raise HTTPException(status_code=400, detail="MedicalRecord not Found")
def get_medical_records(patient_id):
    patient = Patient.find(patient_id)
    if not patient:
        raise HTTPException(status_code=400, detail="Patient not Found")
    return patient.medicalrecords.all()