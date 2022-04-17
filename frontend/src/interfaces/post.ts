export default interface Post {
  id: number,
  user_id: number,
  name: string,
  imageURL: URL,
  description: string,
  created_at: Date
}