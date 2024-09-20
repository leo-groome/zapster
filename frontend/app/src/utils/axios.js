import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://http://127.0.0.1:8000/:8000", // Adjust based on your FastAPI server URL
  headers: {
    "Content-Type": "application/json",
  },
});

export default apiClient;
