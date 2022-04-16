import { combineReducers } from "@reduxjs/toolkit";
import sessionReducer from "./sessionReducer";
import usersReducer from "./usersReducer";

export const rootReducer = combineReducers({sessionReducer, usersReducer});

export type RootState = ReturnType<typeof rootReducer>