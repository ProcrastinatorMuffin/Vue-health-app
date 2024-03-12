import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import PatientMedicalRecords from '../views/MedicalRecords/View.vue'
import PatientMedicalRecords from '../src/views/MedicalRecords/View.vue'
import './assets/main.css'

const app = createApp(App)

app.use(router)
app.component('PatientMedicalRecords', PatientMedicalRecords)
app.mount('#app')
