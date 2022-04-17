import { createAction } from "@reduxjs/toolkit";
import User from "../interfaces/user";

export const ADD_USER = createAction<User, 'addUser'>('addUser');
export const ADD_USERS = createAction<User[], 'addUsers'>('addUsers');