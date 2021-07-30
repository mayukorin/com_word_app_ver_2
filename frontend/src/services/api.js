import axios from "axios";

const api = axios.create({
  baseURL: process.env.VUE_APP_ROOT_API,
  timeout: 1000000,
  headers: {
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",
  },
});

api.interceptors.request.use(
  (config) => {
    /*
    if (token) {
      config.headers.Authorization = "JWT ";
      return config;
    }
    */
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    console.log("error.resposnse=", error.response);
    const status = error.response ? error.response.status : 500;
    console.log(status);
    return Promise.reject(error);
  }
);

export default api;