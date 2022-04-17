import { createReducer, PayloadAction } from "@reduxjs/toolkit";
import User from "../interfaces/user";
import { ADD_USER, ADD_USERS } from "../actions/userActions";

interface UsersState {
  [key: string]: User;
}

const _UsersInitState: UsersState = {};

export default createReducer(_UsersInitState, (builder) => {
  builder
    .addCase(ADD_USER, (state, action: PayloadAction<User>) => {
      state[action.payload.id] = action.payload;
    })
    .addCase(ADD_USERS, (state, action: PayloadAction<User[]>) => {
      const { payload } = action;
      payload.forEach((user) => {
        state[user.id] = user;
      });
    });
});
