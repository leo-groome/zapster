<script>
import Navbar from "./components/Navbar.vue";
import Home from "./components/Home.vue";
import Calendar from "./components/Calendar.vue";
import Account from "./components/Account.vue";

export default {
  name: "App",
  components: {
    Navbar,
    Home,
    Account,
    Calendar,
  },
  data() {
    return {
      currentPage: "home",
    };
  },
  computed: {
    currentComponent() {
      return (
        this.currentPage.charAt(0).toUpperCase() + this.currentPage.slice(1)
      );
    },
  },
};
</script>

<template>
  <div id="app" class="flex w-screen h-screen bg-white">
    <Navbar @change-page="currentPage = $event" class="flex" />
    <main class="flex-grow">
      <component :is="currentComponent"></component>
    </main>
  </div>
</template>

<style>
body {
  font-family: "Nunito", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#app {
  display: flex;
  height: 100vh; /* Make the app full height */
}

main {
  display: flex;
  flex-direction: column; /* Stack child components vertically */
  padding: 16px; /* Add padding for spacing */
}
</style>
