import { createAction } from "@reduxjs/toolkit";
import Post from '../interfaces/post';

export const RECEIVE_POSTS = createAction<Post[], 'receivePosts'>('receivePosts');
export const RECEIVE_POST = createAction<Post, 'receivePost'>('receivePost');


// export const retreievePost = (post) => (dispatch) => {

// }