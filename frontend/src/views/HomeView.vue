<template>
  <main>
    <div class="container">
      <div class="jumbotron">
        <!-- Greeting moved up and changed to <h1> for larger size -->
        <h1 class="greeting">{{ greetingMessage }}</h1>
        <!-- Tracking text now in <h2> and slightly smaller than the greeting -->
        <h2 class="text-center">Track your <RouterLink to="/patients/" class="patients-link">patients</RouterLink> medical records.</h2>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      userName: 'Stranger',
    };
  },
  computed: {
    greetingMessage() {
      const hour = new Date().getHours();
      let greeting;
      if (hour < 12) {
        greeting = 'Good Morning';
      } else if (hour < 18) {
        greeting = 'Good Afternoon';
      } else {
        greeting = 'Good Evening';
      }
      return `${greeting}, ${this.userName}! Welcome to Healthcare App.`;
    },
  },
};
</script>

<style scoped>
.container {
  background-color: #282828;
  color: #ebdbb2;
  padding: 20px;
}

.jumbotron {
  background-color: #3c3836;
  border-radius: 4px;
  padding: 40px;
  text-align: center;
}

/* Style adjustments to reflect the change in element hierarchy */
.greeting {
  color: #ebdbb2;
  font-size: 36px; /* Now larger, as it's the primary greeting */
  margin-bottom: 20px;
}

.text-center {
  color: #ebdbb2;
  font-size: 24px; /* Slightly smaller than the greeting */
  margin-bottom: 20px;
}

.patients-link {
  color: #b8bb26; /* Gruvbox green color for consistency */
  text-decoration: none;
}

.patients-link:hover {
  color: #fabd2f; /* Gruvbox yellow color for hover effect */
  text-decoration: underline;
}
</style>

