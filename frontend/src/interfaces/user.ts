export default interface User {
  id: number,
  username: string,
  email: string,
  avatarURL: URL,
  location: string,
  bio: string,
  dateCreated: Date,
  sessionToken?: string,
};