import axios from "axios";

export default axios.create({
  baseURL: "http://localhost:5000/",
  timeout: 1000,
  headers: { Accept: "application/json " },
});

export interface Data<Type> {
  data: Type
}

export interface APIError{
  error: any
}