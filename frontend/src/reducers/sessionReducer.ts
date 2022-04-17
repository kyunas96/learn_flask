import { createReducer, PayloadAction, Action } from "@reduxjs/toolkit";
import { SESSION_LOGIN, SESSION_LOGOUT } from "../actions/sessionActions";
import User from "../interfaces/user";

interface SessionState {
  userid: number | null;
  sessionToken: string | null | undefined;
}

const _NullSessionState: SessionState = {
  userid: null,
  sessionToken: null,
};

export default createReducer(_NullSessionState, (builder) => {
  builder
    .addCase(SESSION_LOGIN, (state, action: PayloadAction<User>) => {
      const {payload} = action;
      state = {
        userid: payload.id,
        sessionToken: payload.sessionToken
      };
    })
    .addCase(SESSION_LOGOUT, (state, action: Action<string>) => {
      state = _NullSessionState;
    });
});
