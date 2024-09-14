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
  <div id="app" class="flex w-screen bg-white">
    <Navbar @change-page="currentPage = $event" class="flex" />
    <main class="flex">
      <component :is="currentComponent"></component>
    </main>
  </div>
</template>

<style>
body {
  margin: 0;
  font-family: "Montserrat" sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
