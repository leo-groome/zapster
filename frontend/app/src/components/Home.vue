<template>
  <div class="w-fit" id="screen">
    <h1 class="pt-6 pl-6 mb-6 text-4xl text-black border-b border-gray-300">
      Home
    </h1>
    <div class="flex flex-row justify-center items-end mb-4" id="addTask">
      <input
        v-model="newTask"
        class="flex p-2 rounded-md border border-gray-300"
        placeholder="New task"
      />
      <button
        @click="addTask"
        class="flex p-2 ml-2 text-white bg-blue-500 rounded-md"
      >
        Add Task
      </button>
    </div>
    <div id="Tasks" class="flex flex-row">
      <div
        class="flex-col items-center m-1 w-1/3 bg-white border-r border-gray-300"
        id="To-do"
      >
        <h2 class="flex m-2 text-3xl text-start">To-do</h2>
        <draggable v-model="todoTasks" group="tasks" tag="ul">
          <template #item="{ element: task }">
            <li
              class="p-2 m-2 text-white bg-black rounded-md cursor-grab w-fit"
            >
              {{ task }}
            </li>
          </template>
        </draggable>
      </div>
      <div
        class="flex-col m-1 w-1/3 bg-white border-r border-gray-300"
        id="Doing"
      >
        <h2 class="m-2 text-3xl text-start">Doing</h2>
        <draggable v-model="doingTasks" group="tasks" tag="ul">
          <template #item="{ element: task }">
            <li
              class="p-2 m-2 text-white bg-black rounded-md cursor-grab w-fit"
            >
              {{ task }}
            </li>
          </template>
        </draggable>
      </div>
      <div
        class="flex-col m-1 w-1/3 bg-white border-r border-gray-300"
        id="Done"
      >
        <h2 class="m-2 text-3xl text-start">Done</h2>
        <draggable v-model="doneTasks" group="tasks" tag="ul">
          <template #item="{ element: task }">
            <li
              class="p-2 m-2 text-white bg-black rounded-md cursor-grab w-fit"
            >
              {{ task }}
            </li>
          </template>
        </draggable>
      </div>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";

export default {
  name: "Home",
  components: {
    draggable, // Register the draggable component
  },
  data() {
    return {
      todoTasks: ["Walk the dog", "Eat some pizza", "Clean the Kitchen"],
      doingTasks: ["Walk the cat", "Eat some burger", "Clean the Bathroom"],
      doneTasks: ["Walk the Bird", "Eat some tacos", "Clean the dinning room"],
    };
  },
};
</script>
