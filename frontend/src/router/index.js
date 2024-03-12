import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PatientView from '../views/Patient/PatientView.vue'
import PatientCreate from '../views/Patient/PatientCreate.vue'
import PatientGallery from '../views/Patient/PatientGallery.vue'
import PatientAppointments from '../views/Appointment/View.vue'
import PatientMedicalRecords from '../views/MedicalRecords/View.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    }, 
    {
      path: '/patients',
      name: 'patients',
      component: PatientView
      },
      {
      path: '/patients/gallery',
      name: 'PatientGallery',
      component: PatientGallery
      },
      {
      path: '/patient/create',
      name: 'patientCreate',
      component: PatientCreate
      },   
      {
        path: '/patients/:id/appointments',
        name: 'PatientAppointments',
        component: PatientAppointments
        },
      {
          path: '/patients/:id/medicalRecords',
          name: 'PatientMedicalRecords',
          component: PatientMedicalRecords
          },
  ]
})

export default router
