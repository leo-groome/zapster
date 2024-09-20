<template>
  <div class="flex flex-col p-6 h-screen bg-gray-100 rounded-md">
    <h1
      class="mb-6 text-4xl font-bold text-blue-800 border-b-4 border-blue-500"
    >
      Account
    </h1>

    <div class="p-4 bg-white rounded-lg shadow-lg">
      <h2 class="mb-4 text-3xl text-blue-700">Account Details</h2>
      <div class="flex flex-col mb-4">
        <label class="text-gray-600" for="username">Username:</label>
        <input
          id="username"
          type="text"
          class="p-2 rounded-md border border-gray-300 shadow-md"
          placeholder="Your Username"
        />
      </div>
      <div class="flex flex-col mb-4">
        <label class="text-gray-600" for="email">Email:</label>
        <input
          id="email"
          type="email"
          class="p-2 rounded-md border border-gray-300 shadow-md"
          placeholder="Your Email"
        />
      </div>
      <div class="flex flex-col mb-4">
        <label class="text-gray-600" for="password">Password:</label>
        <input
          id="password"
          type="password"
          class="p-2 rounded-md border border-gray-300 shadow-md"
          placeholder="Your Password"
        />
      </div>
      <button
        class="p-3 w-full text-white bg-blue-600 rounded-md shadow-md transition duration-200 hover:bg-blue-700"
      >
        Update Account
      </button>
    </div>

    <div class="p-4 mt-6 bg-white rounded-lg shadow-lg">
      <h2 class="mb-4 text-3xl text-blue-700">Preferences</h2>
      <div class="flex items-center mb-4">
        <input id="notifications" type="checkbox" class="mr-2" />
        <label class="text-gray-600" for="notifications"
          >Receive Notifications</label
        >
      </div>
      <div class="flex items-center mb-4">
        <input id="darkMode" type="checkbox" class="mr-2" />
        <label class="text-gray-600" for="darkMode">Enable Dark Mode</label>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Account",
};
</script>
