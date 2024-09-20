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
        data-status="Todo"
      >
        <h2 class="m-2 text-3xl text-blue-700 text-start">To-do</h2>
        <draggable
          v-model="todoTasks"
          group="tasks"
          @change="onTaskChange('Todo')"
          tag="ul"
        >
          <template #item="{ element: task }">
            <li
              :key="task._id"
              :data-id="task._id"
              class="p-3 m-2 text-white bg-blue-500 rounded-md transition-colors duration-1000 cursor-grab"
            >
              {{ task.title }}
            </li>
          </template>
        </draggable>
      </div>

      <div
        class="flex-col items-center mr-2 w-1/3 bg-yellow-50 rounded-lg border border-yellow-300 shadow-lg"
        data-status="Doing"
      >
        <h2 class="m-2 text-3xl text-yellow-700 text-start">Doing</h2>
        <draggable
          v-model="doingTasks"
          group="tasks"
          @change="onTaskChange('Doing')"
          tag="ul"
        >
          <template #item="{ element: task }">
            <li
              :key="task._id"
              :data-id="task._id"
              class="p-3 m-2 text-white bg-yellow-500 rounded-md transition-colors duration-1000 cursor-grab"
            >
              {{ task.title }}
            </li>
          </template>
        </draggable>
      </div>

      <div
        class="flex-col items-center w-1/3 bg-green-50 rounded-lg border border-green-300 shadow-lg"
        data-status="Done"
      >
        <h2 class="m-2 text-3xl text-green-700 text-start">Done</h2>
        <draggable
          v-model="doneTasks"
          group="tasks"
          @change="onTaskChange('Done')"
          tag="ul"
        >
          <template #item="{ element: task }">
            <li
              :key="task._id"
              :data-id="task._id"
              class="p-3 m-2 text-white bg-green-500 rounded-md transition-colors duration-1000 cursor-grab"
            >
              {{ task.title }}
            </li>
          </template>
        </draggable>
      </div>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";
import axios from "axios";
import { dateFormat } from "vue-cal/dist/i18n/en.cjs";

axios.defaults.baseURL = "http://127.0.0.1:8000/";

export default {
  name: "Home",
  components: {
    draggable,
  },
  data() {
    return {
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
    async fetchTasks() {
      this.loading = true; // Show loading indicator
      try {
        const response = await axios.get(`/users/${this.userId}/tasks`);
        const tasks = response.data;

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

    getCurrentDateTime() {
      const now = new Date();
      const year = now.getFullYear();
      const month = String(now.getMonth() + 1).padStart(2, "0");
      const day = String(now.getDate()).padStart(2, "0");
      const hours = String(now.getHours()).padStart(2, "0");
      const minutes = String(now.getMinutes()).padStart(2, "0");

      return `${year}-${month}-${day}T${hours}:${minutes}`;
    },

    async addTask() {
      // Check if the task input is empty
      if (this.newTask.trim() === "") {
        alert("Please enter a task title");
        return;
      }

      // Construct the task object with empty strings instead of null
      const newTask = {
        title: this.newTask, // Required field
        description: "", // Use empty string instead of null
        due_date: this.getCurrentDateTime(), // Provide an empty string for due_date if no date is selected
        tags: "", // Use an empty string for tags
        status: "Todo", // Default status is 'Todo'
        user_id: this.userId, // User ID is required
      };

      try {
        // Send the POST request to add the new task
        const response = await axios.post(`/tasks/`, newTask);

        // Add the new task to the todoTasks list if successful
        this.todoTasks.push(response.data);

        // Clear the input field after adding the task
        this.newTask = "";
      } catch (error) {
        console.error("Error adding new task:", error);
      }
    },

    async onTaskChange(newStatus) {
      // This event will trigger when a task changes its position in a new list
      // We know the new status because we pass it as an argument in the @change event

      console.log(`Task moved to: ${newStatus}`);

      // Find the task that was moved
      // Since `vuedraggable` updates the `v-model`, we can find out which task is now in this list
      const updatedTaskLists = {
        Todo: this.todoTasks,
        Doing: this.doingTasks,
        Done: this.doneTasks,
      };

      // Loop over each updated task list
      Object.entries(updatedTaskLists).forEach(([status, tasks]) => {
        tasks.forEach(async (task) => {
          // If a task now belongs to the new status category, update the status in the database
          if (status === newStatus) {
            console.log(`Updating task ${task._id} to ${newStatus}`);
            await this.updateTaskStatus(task._id, newStatus);
          }
        });
      });
    },

    async updateTaskStatus(taskId, newStatus) {
      try {
        const response = await axios.put(
          `http://127.0.0.1:8000/tasks/${taskId}`,
          {
            status: newStatus,
          }
        );
        console.log("Task status updated:", response.data);
      } catch (error) {
        console.error("Error updating task status:", error);
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
