import APIClient, { Data } from "./axiosBase";
import User from "../interfaces/user";

interface LoginData {
  username: string;
  password: string;
}

const login = async (username: string, password: string) =>{
  const formData = new FormData();
  formData.append('username', username)
  formData.append('password', password)
  return APIClient.post("session/login", formData);
}

const logout = async () =>
  APIClient.post("/session/logout");

export { login, logout };
