import axios from "axios";
import { API_BASE_URL } from "../constants/apiConstants";

export const BaseService = axios.create({
  baseURL: API_BASE_URL,
});

BaseService.interceptors.request.use((config) => {
  const access_token = localStorage.getItem("accessToken");
  if (access_token) {
    config.headers.Authorization = `Bearer ${access_token}`;
  }
  return config;
});

BaseService.interceptors.response.use((response) => {
  console.log(response);
  return response;
});
