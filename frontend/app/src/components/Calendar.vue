<template>
  <div class="flex flex-col p-6 h-screen bg-gray-100 rounded-md">
    <h1
      class="mb-6 text-4xl font-bold text-blue-800 border-b-4 border-blue-500"
    >
      Calendar
    </h1>
    <div class="flex flex-col">
      <h2 class="mb-4 text-3xl text-blue-700">Task Calendar</h2>
      <div class="p-4 bg-white rounded-lg shadow-lg">
        <vue-cal
          style="height: 32rem; border-radius: 0.5rem"
          default-view="week"
          :time="true"
          :weekdays="[1, 2, 3, 4, 5, 6, 0]"
        />
      </div>
    </div>
  </div>
</template>

<script>
import VueCal from "vue-cal";
import "vue-cal/dist/vuecal.css";

export default {
  name: "Calendar",
  components: {
    VueCal, // Register the Vue Cal component
  },
};
</script>

<style scoped>
/* Add any specific styles for the calendar here, if needed */
</style>
