import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1",
  timeout: 10000,
});

export const getNews = () => api.get("/news");
export const searchNews = (q) => api.get(`/search?q=${q}`);
export const getAnalytics = () => api.get("/analytics/analytics/trends");

export default api;
