<template>
  <div class="w-fit" id="screen">
    <h1 class="pt-6 pl-6 mb-6 text-4xl text-black border-b border-gray-300">
      Calendar
    </h1>
    <div id="calendar" class="flex flex-col ml-3">
      <h2 class="text-3xl text-black">Task Calendar</h2>
      <vue-cal
        style="height: 32rem"
        default-view="week"
        :time="true"
        :weekdays="[1, 2, 3, 4, 5, 6, 0]"
      />
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
