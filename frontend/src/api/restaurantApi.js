import axios from "axios";

const API_URL = "http://localhost:8080/api/v1/restaurants/all/";

export function getAllRestaurants() {
  return axios.get(API_URL).then(res => res.data);
}
