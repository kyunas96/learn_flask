import { createAction } from "@reduxjs/toolkit";
import User from "../interfaces/user";

export const SESSION_LOGIN = createAction<User, 'sessionLogin'>('sessionLogin');
export const SESSION_LOGOUT = createAction<'sessionLogout'>('sessionLogout');
