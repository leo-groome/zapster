/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}", // Includes all Vue, JS, and TS files in your src folder
  ],
  theme: {
    extend: {
      colors: {
        navwhite: "#F8F8F8",
      },
      fontFamily: {
        sans: ["Inter", "Arial", "sans-serif"],
      },
    },
  },
  plugins: [],
};
