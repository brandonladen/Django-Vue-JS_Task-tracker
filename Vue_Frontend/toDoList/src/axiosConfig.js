import axios from 'axios';

const baseURL = 'http://localhost:8000';

const axiosInstance = axios.create({
  baseURL: baseURL,
  timeout: 360000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor to include token in the headers if available
axiosInstance.interceptors.request.use(
  config => {
    const token = sessionStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Token ${token}`;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

// Response interceptor to store token from login response
axiosInstance.interceptors.response.use(
  response => {
    // Check if the response contains a token
    if (response.data && response.data.token) {
      const token = response.data.token;
      // Store the token in sessionStorage
      sessionStorage.setItem('token', token);
    }
    return response;
  },
  error => {
    return Promise.reject(error);
  }
);

export default axiosInstance;
