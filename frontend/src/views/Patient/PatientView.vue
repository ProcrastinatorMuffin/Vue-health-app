<template>
    <div class="wrapper">
    <div class="container">
      <div class="card">
        <div class="card-header">
          <h4>
            Patients
            <RouterLink to="/patient/create" class="btn btn-primary float-end">Add Patient</RouterLink>
            <RouterLink to="/patients/gallery" class="btn btn-success float-end view-gallery">View Gallery</RouterLink>
          </h4>
        </div>
        <div class="card-body">
          <table class="table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Date of Birth</th>
                <th>Phone Number</th>
                <th>Gender</th>
                <th>Address</th>
                <th>Status</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody v-if="patients.length > 0">
              <tr v-for="(patient, index) in patients" :key="index">
                <td>{{ patient.id }}</td>
                <td>{{ patient.name }}</td>
                <td>{{ patient.email }}</td>
                <td>{{ patient.dob }}</td>
                <td>{{ patient.phone_number }}</td>
                <td>{{ patient.gender }}</td>
                <td>{{ patient.address }}</td>
                <td>{{ patient.status }}</td>
                <td>
                  <div class="action-buttons">
                    <RouterLink :to="{ path: '/patients/' + patient.id + '/appointments' }" class="btn btn-success view-data">
                      View Data
                    </RouterLink>
                    <button type="button" @click="deletePatient(patient.id)" class="btn btn-danger">
                      Enable/Disable
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
            <tbody v-else>
              <tr>
                <td colspan="9">Loading...</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
</div>
  </template>
  
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'patients',
    data() {
      return {
        patients: []
      }
    },
    mounted() {
      this.getPatients();
    },
    methods: {
      getPatients() {
        axios.get(`http://${import.meta.env.VITE_BASE_URL}:3000/patients/`).then(res => {
          this.patients = res.data
          console.log(this.patients)
        });
      },
      deletePatient(patientId) {
        if (confirm('Are you sure you want to disable?')) {
          axios.put(`http://${import.meta.env.VITE_BASE_URL}:3000/patients/${patientId}`)
            .then(res => {
              this.getPatients()
            });
        }
      }
    }
  }
  </script>
  
  <style scoped>

html, body {
  margin: 0;
  padding: 0;
}

.wrapper {
  display: flex;
  justify-content: center;
  width: 100%;
}

.container {
  background-color: #282828;
  color: #ebdbb2;
  padding: 20px;
  width: 100%; /* Ensure it takes the full width */
  max-width: 95%; /* Max width to maintain a margin from the viewport edge */
  margin: auto; /* Center the container */
}

.card {
  background-color: #3c3836;
  border: none;
  padding: 0;
  margin-bottom: 20px;
  width: auto;
  max-width: 100%;
}

.card-header, .card-body {
  padding: 10px; /* Apply consistent padding to both header and body */
  box-sizing: border-box; /* Ensure padding is included in the total width */
}

.card-body {
  overflow-x: auto; /* Add horizontal scroll on overflow */
}

.card-header {
  background-color: #504945;
}

.card-header h4 {
  margin: 0;
}

.table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.table th, .table td {
  padding: 12px;
  text-align: center;
  border: 1px solid #665c54;
}

.table th {
  background-color: #665c54;
  color: #ebdbb2;
}

.btn {
  background-color: #689d6a;
  border: none;
  color: #ebdbb2;
  padding: 8px 16px;
  margin: 0 5px;
  cursor: pointer;
  font-family: 'JetBrains Mono', monospace;
  display: inline-block;
}

.btn-primary {
  background-color: #458588;
}

.btn-success {
  background-color: #98971a;
}

.btn-danger {
  background-color: #cc241d;
}

.action-buttons {
  display: flex;
  justify-content: center;
  gap: 10px;
}

.view-data, .btn-danger {
  flex: 1;
}


</style>

