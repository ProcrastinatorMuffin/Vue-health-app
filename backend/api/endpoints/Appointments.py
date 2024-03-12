from fastapi import HTTPException
from models.Appointment import Appointment
from models.Patient import Patient
import schema

def get_all():
    appointments = Appointment.all()
    return appointments.all()
def add(appointment_data: schema.AppointmentBase):
    patient = Patient.find(appointment_data.patient_id)
    if not patient:
        raise HTTPException(status_code=400, detail="Patient not Found")
    appointment = Appointment()
    appointment.date = appointment_data.date
    appointment.doctor = appointment_data.doctor
    appointment.notes = appointment_data.notes
    appointment.patient_id = appointment_data.patient_id
    appointment.save()
    return appointment
def get(appointment_id: int):
    appointment = Appointment.find(appointment_id)
    if not appointment:
        raise HTTPException(status_code=400, detail="Appointment not Found")
    return appointment
def delete(appointment_id: str):
    appointment =  Appointment.find(appointment_id)
    if appointment:
        appointment.delete()
        return appointment
    else:
        raise HTTPException(status_code=400, detail="Appointment not Found")
def get_appointments(patient_id):
    patient = Patient.find(patient_id)
    if not patient:
        raise HTTPException(status_code=400, detail="Patient not Found")
    return patient.appointments.all()