from fastapi import FastAPI
from typing import List
import schema
from fastapi.responses import RedirectResponse
from endpoints import Patients
from endpoints import Appointments
from endpoints import MedicalRecords
from endpoints import Medications
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def docs_redirect():
    response = RedirectResponse(url='/docs')
    return response

# For Patients
@app.get("/patients/", response_model=List[schema.PatientResult])
def get_all_patients():
    return Patients.get_all()
@app.post("/patients/", response_model=schema.PatientResult)
def add_patient(patient_data: schema.PatientBase):
    return Patients.add(patient_data)
@app.get("/patients/{patient_id}", response_model=schema.PatientResult)
def get_single_patient(patient_id: int):
    patient =  Patients.get(patient_id)
    return patient
@app.delete("/patients/{patient_id}", response_model=schema.PatientResult)
def delete_patient(patient_id: str):
    return Patients.delete(patient_id)
@app.put("/patients/{patient_id}", response_model=schema.PatientResult)
def disable_patient(patient_id: str):
    patient = get_single_patient(patient_id)
    if patient:
        return Patients.disable(patient_id)



# For Appointment
@app.get("/appointments/", response_model=List[schema.AppointmentResult])
def get_all_appointment():
    return Appointments.get_all()
@app.post("/appointments/", response_model=schema.AppointmentResult)
def add_appointment(appointment_data: schema.AppointmentBase):
    return Appointments.add(appointment_data)
@app.get("/appointments/{appointment_id}", response_model=schema.AppointmentResult)
def get_single_appointment(appointment_id: int):
    return Appointments.get(appointment_id)
@app.delete("/appointment/{appointment_id}", response_model=schema.AppointmentResult)
def delete_appointment(appointment_id: str):
    return Appointments.delete(appointment_id)
@app.get("/patients/{patient_id}/appointments/", response_model=List[schema.AppointmentResult])
def get_patient_appointments(patient_id):
    return Appointments.get_appointments(patient_id)

# For Medical Records
@app.get("/medical_records/", response_model=List[schema.MedicalRecordResult])
def get_all_medical_records():
    return MedicalRecords.get_all()
@app.post("/medical_records/", response_model=schema.MedicalRecordResult)
def add_medical_records(medical_records_data: schema.MedicalRecordBase):
    return MedicalRecords.add(medical_records_data)
@app.get("/medical_records/{medical_records_id}", response_model=schema.MedicalRecordResult)
def get_single_medical_records(medical_records_id: int):
    return MedicalRecords.get(medical_records_id)
@app.delete("/medical_records/{medical_records_id}", response_model=schema.MedicalRecordResult)
def delete_medical_records(medical_records_id: str):
    return MedicalRecords.delete(medical_records_id)
@app.get("/patients/{patient_id}/medical_records/", response_model=List[schema.MedicalRecordResult])
def get_patient_medical_records(patient_id):
    return MedicalRecords.get_medical_records(patient_id)

# For Medication
@app.get("/medication/", response_model=List[schema.MedicationResult])
def get_all_medication():
    return Medications.get_all()
@app.post("/medication/", response_model=schema.MedicationResult)
def add_medication(medication_data: schema.MedicationBase):
    return Medications.add(medication_data)
@app.get("/medication/{medication_id}", response_model=schema.MedicationResult)
def get_single_medication(medication_id: int):
    return Medications.get(medication_id)
@app.delete("/medication/{medication_id}", response_model=schema.MedicationResult)
def delete_medication(medication_id: str):
    return Medications.delete(medication_id)
@app.get("/patients/{patient_id}/medication/", response_model=List[schema.MedicationResult])
def get_patient_medication(patient_id):
    return Medications.get_medication(patient_id)