import APIClient, { Data } from "./axiosBase";
import Post from "../interfaces/post";

export const retreievePost = (postId: number) =>
  APIClient.get(`/posts/${postId}`);

// API CALLS FOR FEED
export const retrieveFeedPosts = (pageNum: number) =>
  APIClient.get(`/feed/${pageNum}`);

export const retrieveUsersPosts = (userId: number, pageNum: number) =>
  APIClient.get(`/users/${userId}/${pageNum}`);
