<script>
import axios from 'axios'
export default {
  name: 'patientAppointments',
  data() {
    return {
      medicalRecords: []
    }
  },
  mounted() {
    this.getMedicalRecords();
  },
  methods: {
    getMedicalRecords() {
      const value = this.$route.params.id;
      axios.get(`http://${import.meta.env.VITE_BASE_URL}:3000/patients/${value}/medical_records/`)
        .then(res => {
          this.medicalRecords = res.data
        });
    },
    deleteMedicalRecords(medicalRecordsId) {
      if (confirm('Are you sure you want to delete?')) {
        axios.delete(`http://${import.meta.env.VITE_BASE_URL}:3000/appointment/${medicalRecordsId}/`)
          .then(res => {
            this.getMedicalRecords()
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
          <h4>Medical Records</h4>
        </div>
        <div class="card-body">
          <table class="table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Date</th>
                <th>Diagnosis</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody v-if="this.medicalRecords.length > 0">
              <tr v-for="(medicalRecord, index) in this.medicalRecords" :key="index">
                <td>{{ medicalRecord.id }}</td>
                <td>{{ medicalRecord.date }}</td>
                <td>{{ medicalRecord.diagnosis }}</td>
                <td>
                  <button type="button" @click="deleteMedicalRecords(medicalRecord.id)" class="btn btn-danger">
                    Delete
                  </button>
                </td>
              </tr>
            </tbody>
            <tbody v-else>
              <tr>
                <td colspan="4">No Medical Records...</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <PatientView />
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
.table td:nth-child(2) {
  width: 1%;
  white-space: nowrap;
}

.table th:nth-child(3),
.table td:nth-child(3) {
  width: auto;
}

.table th:last-child,
.table td:last-child {
  border-right: 1px solid #504945;
  width: 100px;
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
  max-width: 100px;
}
</style>