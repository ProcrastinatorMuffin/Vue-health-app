<template>
    <div class="wrapper">
    <div class="container">
      <main>
        <div class="header">
          <h4>
            Patients
            <RouterLink to="/patient/create" class="btn btn-primary">Add Patient</RouterLink>
            <RouterLink to="/patients" class="btn btn-success">View Table</RouterLink>
          </h4>
        </div>
        <div class="card-grid">
          <div v-for="(patient, index) in this.patients" :key="index" class="card">
            <div class="card-image">
              <img :src="patient.gender === 'male' ? '/src/assets/male.jpg' : '/src/assets/female.jpg'" alt="Card image cap">
            </div>
            <div class="card-body">
              <div class="row">
                <div class="col-label">Name</div>
                <div class="col-value">{{ patient.name }}</div>
              </div>
              <div class="row">
                <div class="col-label">Email</div>
                <div class="col-value">{{ patient.email }}</div>
              </div>
              <div class="row">
                <div class="col-label">Date of Birth</div>
                <div class="col-value">{{ patient.dob }}</div>
              </div>
              <div class="row">
                <div class="col-label">Gender</div>
                <div class="col-value">{{ patient.gender }}</div>
              </div>
              <div class="row">
                <div class="col-label">Phone</div>
                <div class="col-value">{{ patient.phone_number }}</div>
              </div>
              <div class="row">
                <div class="col-label">Address</div>
                <div class="col-value">{{ patient.address }}</div>
              </div>
              <div class="row">
                <div class="col-label">Status</div>
                <div class="col-value">{{ patient.status }}</div>
              </div>
              <div class="card-actions">
                <RouterLink :to="{ path: '/patients/' + patient.id + '/appointments' }" class="btn btn-success">
                  View Data
                </RouterLink>
                <button type="button" @click="deletePatient(patient.id)" class="btn btn-danger">
                  Disable/Enable
                </button>
              </div>
            </div>
          </div>
        </div>
      </main>
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
.wrapper {
  display: flex;
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

.header, .card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  background-color: #504945;
  padding: 15px 15px; /* Increase padding for more space */
  box-sizing: border-box;
}

.card-header h4, .header h4 {
  margin: 0;
  color: #ebdbb2; /* Ensuring text color consistency */
}


.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  width: 100%; /* Ensure the grid takes up full container width */
}

.card {
  background-color: #3c3836;
  padding: 20px;
}

.card-image {
  text-align: center;
  margin-bottom: 10px;
}

.card-image img {
  max-width: 100%;
  height: auto;
}

.row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 5px;
  border-bottom: 1px solid #575757; /* Subtle border color */
  padding: 5px 0; /* Adjust padding as needed */
}

.col-6 {
  flex-basis: 50%;
}

.card-actions {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.btn {
  background-color: #689d6a;
  border: none;
  color: #ebdbb2;
  padding: 8px 16px;
  text-decoration: none;
  margin-right: 10px;
  cursor: pointer;
  transition: background-color 0.3s;
  border-radius: 0; /* Ensure sharp edges */
}

.btn:hover {
  background-color: #8ec07c;
}

.btn-primary {
  background-color: #458588;
}

.btn-primary:hover {
  background-color: #83a598;
}

.btn-success {
  background-color: #98971a;
}

.btn-success:hover {
  background-color: #b8bb26;
}

.btn-danger {
  background-color: #cc241d;
  font-family: 'JetBrains Mono', monospace; /* Apply JetBrains Mono font */
}

.btn-danger:hover {
  background-color: #fb4934;
}
</style>
