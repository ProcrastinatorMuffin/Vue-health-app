from fastapi import HTTPException
from models.Patient import Patient
from models.Appointment import Appointment
import schema
def get_all():
    patients = Patient.all()
    return patients.all()
def add(patient_data: schema.PatientBase):
    patient = Patient.where("email", patient_data.email).get()
    if patient:
        raise HTTPException(status_code=400, detail="Patient already exists")
    patient = Patient()
    patient.email = patient_data.email
    patient.name = patient_data.name
    patient.dob = patient_data.dob
    patient.phone_number = patient_data.phone_number
    patient.gender = patient_data.gender
    patient.address = patient_data.address
    patient.status = "Enabled"
    patient.save()
    return patient
def get(patient_id: int):
    patient = Patient.find(patient_id)
    if not patient:
        raise HTTPException(status_code=400, detail="Patient not Found")
    return patient
def delete(patient_id: str):
    patient =  Patient.find(patient_id)
    if patient:
        patient.delete()
        return patient
    else:
        raise HTTPException(status_code=400, detail="Patient not Found")

def disable(patient_id: str):
    patient = Patient.find(patient_id)
    if(patient.status == "Enabled"):
        patient.status = "Disabled"
    else:
        patient.status = "Enabled"
    patient.save()
    return patient
