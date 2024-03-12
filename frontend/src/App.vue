<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav>
      <div class="container">
        <RouterLink class="logo" to="/">Healthcare Application</RouterLink>
        <ul class="nav-links">
          <li>
            <RouterLink to="/patients/">Patients</RouterLink>
          </li>
        </ul>
      </div>
    </nav>
  </header>
  <RouterView />
</template>

<style scoped>
header {
  background-color: #282828; /* Gruvbox dark background color */
  padding: 0.5rem 0; /* Reduced padding */
  width: 100%;
}

.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0 1rem; /* Closer to the edge, adjust as needed */
}

.logo {
  color: #ebdbb2; /* Gruvbox light text color */
  font-size: 1.8rem; /* Increased font size */
  font-weight: bold;
  text-decoration: none;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 1.5rem; /* Increased gap */
}

.nav-links a {
  color: #b8bb26; /* Gruvbox green, for better visibility and match */
  text-decoration: none;
  font-size: 1.2rem; /* Increased font size */
  padding: 0.5rem; /* Larger clickable area */
}

.nav-links a:hover {
  text-decoration: none;
  color: #fabd2f; /* Gruvbox yellow, for hover effect */
}
</style>
