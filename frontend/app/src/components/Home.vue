<template>
  <div class="flex flex-col h-screen bg-gray-100 rounded-md">
    <h1
      class="inline-block overflow-hidden pt-6 pl-6 mb-6 max-w-full text-4xl font-bold text-blue-800 border-b-4 border-blue-500"
    >
      Home
    </h1>

    <div class="flex justify-center mb-4" id="addTask">
      <input
        v-model="newTask"
        class="p-3 w-1/3 rounded-md border border-gray-300 shadow-md"
        placeholder="New task"
      />
      <button
        @click="addTask"
        class="p-3 ml-2 text-white bg-blue-600 rounded-md shadow-md transition duration-200 hover:bg-blue-700"
      >
        Add Task
      </button>
    </div>
    <div class="flex flex-row flex-grow justify-between p-4">
      <div
        class="flex-col items-center mr-2 w-1/3 bg-blue-50 rounded-lg border border-blue-300 shadow-lg"
      >
        <h2 class="m-2 text-3xl text-blue-700 text-start">To-do</h2>
        <!-- <draggable v-model="todoTasks" group="tasks" tag="ul">
          <template #item="{ element: task, index }">
            <li
              :key="task.id"
              :class="[
                'p-3 m-2 rounded-md cursor-grab transition-colors duration-1000',
                { 'bg-blue-500 text-white': true },
              ]"
            >
              {{ task.name }}
            </li>
          </template>
        </draggable> -->
        <draggable v-model="todoTasks" group="tasks" tag="ul">
          <template #item="{ element: task, index }">
            <li
              :key="task._id"
              :class="[
                'p-3 m-2 rounded-md cursor-grab transition-colors duration-1000',
                { 'bg-blue-500 text-white': true },
              ]"
            >
              {{ task.title }}
            </li>
          </template>
        </draggable>
      </div>
      <div
        class="flex-col items-center mr-2 w-1/3 bg-yellow-50 rounded-lg border border-yellow-300 shadow-lg"
      >
        <h2 class="m-2 text-3xl text-yellow-700 text-start">Doing</h2>
        <draggable v-model="doingTasks" group="tasks" tag="ul">
          <template #item="{ element: task, index }">
            <li
              :key="task.id"
              :class="[
                'p-3 m-2 rounded-md cursor-grab transition-colors duration-1000',
                { 'bg-yellow-500 text-white': true },
              ]"
            >
              {{ task.name }}
            </li>
          </template>
        </draggable>
      </div>
      <div
        class="flex-col items-center w-1/3 bg-green-50 rounded-lg border border-green-300 shadow-lg"
      >
        <h2 class="m-2 text-3xl text-green-700 text-start">Done</h2>
        <draggable v-model="doneTasks" group="tasks" tag="ul">
          <template #item="{ element: task, index }">
            <li
              :key="task.id"
              :class="[
                'p-3 m-2 rounded-md cursor-grab transition-colors duration-1000',
                { 'bg-green-500 text-white': true },
              ]"
            >
              {{ task.name }}
            </li>
          </template>
        </draggable>
      </div>
    </div>
  </div>
  <p>{{ todoTask }}</p>
</template>

<script>
import draggable from "vuedraggable";
import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:8000/";

export default {
  name: "Home",
  components: {
    draggable,
  },
  data() {
    return {
      // newTask: "",
      // todoTasks: [
      //   { id: 1, name: "Walk the dog" },
      //   { id: 2, name: "Eat some pizza" },
      //   { id: 3, name: "Clean the Kitchen" },
      // ],
      // doingTasks: [
      //   { id: 4, name: "Walk the cat" },
      //   { id: 5, name: "Eat some burger" },
      //   { id: 6, name: "Clean the Bathroom" },
      // ],
      // doneTasks: [
      //   { id: 7, name: "Walk the Bird" },
      //   { id: 8, name: "Eat some tacos" },
      //   { id: 9, name: "Clean the dining room" },
      // ],
      userId: "66ec8f44442a61ac3c243ba6", // example user ID
      newTask: "",
      todoTasks: [],
      doingTasks: [],
      doneTasks: [],
      loading: false, // For showing loading state
    };
  },
  mounted() {
    this.fetchTasks();
  },
  methods: {
    // addTask() {
    //   if (this.newTask) {
    //     const newTask = { id: Date.now(), name: this.newTask };
    //     this.todoTasks.push(newTask);
    //     this.newTask = ""; // Clear input after adding
    //   }
    // },
    async fetchTasks() {
      this.loading = true; // Show loading indicator
      try {
        console.log("Fetching tasks for user ID:", this.userId);
        const response = await axios.get(`/users/${this.userId}/tasks`);
        const tasks = response.data;
        console.log("Fetched tasks:", tasks);

        // Organize tasks by status
        this.todoTasks = tasks.filter((task) => task.status === "Todo");
        this.doingTasks = tasks.filter((task) => task.status === "Doing");
        this.doneTasks = tasks.filter((task) => task.status === "Done");
      } catch (error) {
        console.error("Error fetching tasks:", error);
      } finally {
        this.loading = false; // Hide loading indicator
      }
    },
  },
};
</script>

<style scoped>
#Tasks {
  overflow-y: auto; /* Allows scrolling if tasks exceed height */
}
</style>
