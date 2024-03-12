<template>
  <div class="container">
    <div class="card">
      <div class="card-header">
        <h4 class="text-center">Add Patient</h4>
      </div>
      <div class="card-body">
        <div class="form-group">
          <label for="name">Name</label>
          <input type="text" id="name" v-model="model.patient.name" class="form-control text-center" placeholder="Patient's name">
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <input type="text" id="email" v-model="model.patient.email" class="form-control text-center" placeholder="Patient's email">
        </div>
        <div class="form-group">
          <label for="dob">Date of Birth</label>
          <input type="text" id="dob" v-model="model.patient.dob" @input="formatDate" placeholder="dd/mm/yy" class="form-control text-center">
        </div>
        <div class="form-group">
          <label for="phone">Phone Number</label>
          <input type="text" id="phone" v-model="model.patient.phone_number" class="form-control text-center" placeholder="Patient's phone number">
        </div>
        <div class="form-group">
          <label for="gender">Gender</label>
          <select id="gender" class="form-control text-center" v-model="model.patient.gender" name="genders" form="carform">
            <option value="" disabled selected>Select gender</option>
            <option>male</option>
            <option>female</option>
          </select>
        </div>
        <div class="form-group">
          <label for="address">Address</label>
          <input type="text" id="address" v-model="model.patient.address" class="form-control text-center" placeholder="Patient's address">
        </div>
        <div class="form-actions">
          <button type="button" @click="savePatient" class="btn btn-primary btn-block">Save</button>
          <RouterLink to="/patients" class="btn btn-secondary btn-block">Cancel</RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'patientCreate',
  data() {
    return {
      model: {
        patient: {
          name: '',
          email: '',
          dob: '',
          phone_number: '',
          gender: '',
          address: '',
          status: ''
        }
      }
    }
  },
  methods: {
    savePatient() {
      axios.post(`http://${import.meta.env.VITE_BASE_URL}:3000/patients/`, this.model.patient)
        .then(res => {
          this.$router.push({ path: '/patients/gallery', replace: true })
        });
    },
    formatDate() {
      let dob = this.model.patient.dob.replace(/\D/g, '');
      if (dob.length > 2) {
        dob = dob.slice(0, 2) + '/' + dob.slice(2);
      }
      if (dob.length > 5) {
        dob = dob.slice(0, 5) + '/' + dob.slice(5, 7);
      }
      this.model.patient.dob = dob;
    }
  }
}
</script>
  
  <style scoped>
.container {
  background-color: #282828;
  color: #ebdbb2;
  padding: 20px;
  max-width: 95%;
  margin: auto; /* This already centers the container horizontally */
}

.card {
  background-color: #3c3836;
  border: none;
  border-radius: 4px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
  margin: 20px auto; /* Center the card within the container */
  width: auto; /* Allow the card to expand based on its content */
}

/* Ensuring form groups and actions are also centered */
.form-group, .form-actions {
  text-align: center; /* Center the content of form groups and form actions */
}

.form-group {
  margin-bottom: 20px; /* Ensure adequate spacing between form elements */
}

.form-group label {
  color: #ebdbb2; /* Ensure label color matches the theme */
}

/* Since form controls and buttons are block-level elements, their parent containers control their centering */
.form-control, .btn {
  display: inline-block; /* Change to inline-block if necessary for alignment */
  margin: 0 auto; /* Center form controls and buttons if they don't occupy full width */
}

/* Adjust input, select, and textarea elements to ensure they are properly aligned */
input.form-control, select.form-control, textarea.form-control {
  width: 100%; /* Adjust width to ensure elements are not too wide */
  margin: 0 auto; /* Centering form controls */
}

.form-control {
  width: 100%; /* Full width to use the available space */
  padding: 0.5rem;
  background-color: #282828;
  color: #ebdbb2;
  border: 1px solid #504945;
  border-radius: 4px;
  font-family: 'JetBrains Mono', monospace; /* Maintain font consistency */
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 20px;
}

.btn {
  font-family: 'JetBrains Mono', monospace; /* Ensure consistent font */
  display: inline-block; /* Keep buttons inline */
  text-align: center; /* Center text within buttons */
}

.text-center {
  text-align: center;
}

.btn-block {
  display: block;
  width: 100%;
}

.btn-primary, .btn-secondary {
  border: none;
  border-radius: 4px;
  padding: 8px 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-primary {
  background-color: #b8bb26;
  color: #282828;
}

.btn-primary:hover {
  background-color: #98971a;
}

.btn-secondary {
  background-color: #504945;
  color: #ebdbb2;
  text-decoration: none;
}

.btn-secondary:hover {
  background-color: #3c3836;
}
</style>

