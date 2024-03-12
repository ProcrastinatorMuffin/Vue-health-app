<script>
import axios from 'axios'
import PatientMedicalRecords from '../MedicalRecords/View.vue'

export default {
  name: 'patientAppointments',
  data() {
    return {
      appointments: []
    }
  },
  mounted() {
    this.getAppointments();
  },
  methods: {
    getAppointments() {
      const value = this.$route.params.id;
      axios.get(`http://${import.meta.env.VITE_BASE_URL}:3000/patients/${value}/appointments/`)
        .then(res => {
          this.appointments = res.data
        });
    },
    deleteAppointment(appointmentid) {
      if (confirm('Are you sure you want to delete?')) {
        axios.delete(`http://${import.meta.env.VITE_BASE_URL}:3000/appointment/${appointmentid}/`)
          .then(res => {
            this.getAppointments()
          });
      }
    }
  }
}
</script>

<template>
  <div class="container">
    <div class="card">
      <div class="card-header">
        <h4>Appointments</h4>
      </div>
      <div class="card-body">
        <table class="table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Date</th>
              <th>Doctor</th>
              <th>Notes</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody v-if="this.appointments.length > 0">
            <tr v-for="(appointment, index) in this.appointments" :key="index">
              <td>{{ appointment.id }}</td>
              <td>{{ appointment.date }}</td>
              <td>{{ appointment.doctor }}</td>
              <td>{{ appointment.notes }}</td>
              <td>
                <button type="button" @click="deleteAppointment(appointment.id)" class="btn btn-danger">
                  Delete
                </button>
              </td>
            </tr>
          </tbody>
          <tbody v-else>
            <tr>
              <td colspan="5">No Appointments...</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <PatientMedicalRecords />
</template>

<style scoped>
.container {
  background-color: #282828;
  color: #ebdbb2;
  padding: 20px;
}

.card {
  background-color: #3c3836;
  border-radius: 4px;
  padding: 20px;
}

.card-header {
  margin-bottom: 20px;
}

.table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  margin-bottom: 20px;
  border: 1px solid #504945;
}

.table th,
.table td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #504945;
  border-right: 1px solid #504945;
}

.table th:nth-child(1),
.table td:nth-child(1),
.table th:nth-child(2),
.table td:nth-child(2),
.table th:nth-child(3),
.table td:nth-child(3) {
  width: 1%;
  white-space: nowrap;
}

.table th:last-child,
.table td:last-child {
  border-right: 1px solid #504945;
  width: 100px; /* Adjust the width as needed */
  white-space: nowrap;
}

.table th {
  background-color: #504945;
  color: #ebdbb2;
}

.btn {
  background-color: #689d6a;
  border: none;
  color: #ebdbb2;
  padding: 8px 16px;
  text-decoration: none;
  cursor: pointer;
}

.btn-danger {
  background-color: #cc241d;
  font-family: 'JetBrains Mono', monospace;
  width: 100%;
}
</style>
