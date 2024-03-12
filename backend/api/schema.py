from pydantic import BaseModel
from typing import List, Optional

# For Patient
class PatientBase(BaseModel):
    name: str
    email: str
    dob: str
    phone_number: str
    gender: str
    status: str
    address: Optional[str] = None
class PatientResult(PatientBase):
    id: int
    class Config:
      orm_mode = True


# For Appointment
class AppointmentBase(BaseModel):
   date: str
   notes: str
   doctor: str
   patient_id: int
class AppointmentResult(AppointmentBase):
    id: int
    class Config:
      orm_mode = True

# For Medical Reocrds
class MedicalRecordBase(BaseModel):
   date: str
   diagnosis: str
   patient_id: int
class MedicalRecordResult(MedicalRecordBase):
    id: int
    class Config:
      orm_mode = True

# For Medication
class MedicationBase(BaseModel):
    name: str
    dosage: str
    frequency: str
    start_date: str
    end_date: str
    patient_id: int
    medicalrecord_id: int
class MedicationResult(MedicationBase):
    id: int
    class Config:
      orm_mode = True



