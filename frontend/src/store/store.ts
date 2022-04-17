import {
  configureStore,
  AnyAction,
  MiddlewareArray,
  Middleware,
} from "@reduxjs/toolkit";
import { rootReducer, RootState } from "../reducers/rootReducer";
import thunk, { ThunkDispatch, ThunkMiddleware } from "redux-thunk";

const thunkMW: ThunkMiddleware<RootState, AnyAction> = thunk;

// const middleWare: MiddlewareArray = applyMiddleware()

const store = configureStore({
  reducer: rootReducer,
  middleware: (defaultMiddleWares) => defaultMiddleWares().concat(thunkMW)
});

// export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;
