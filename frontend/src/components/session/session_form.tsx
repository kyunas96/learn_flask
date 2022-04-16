import React, { useState } from "react";
import { login } from "../../API/sessionAPI";
import { AxiosError } from "axios";
import SessionError from "./session_form_errors";

interface Error {
  error: string
}


const SessionForm = () => {
  const [username, setUsername] = useState<string>("")
  const [password, setPassword] = useState<string>("")
  const [usernamePresent, setUsernamePresent] = useState<boolean>(true);
  const [passwordPresent, setPasswordPresent] = useState<boolean>(true);
  const [loginerrors, setLoginErrors] = useState<string>("");

  const handleChange = (fn: Function): React.ChangeEventHandler<HTMLInputElement> => {
    return (e) => fn(e.target.value)
  }

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    resetErrors()
    if (validateFields()) {
      try {
        const user = await login(username, password)
        console.log(user)
      } catch (err: any) {
        const { error } = (err as AxiosError<Error>).response?.data || {}
        setLoginErrors(error || "");
      }
    }
  }

  const validateFields = () => {
    if(username === "") setUsernamePresent(false);
    if(password === "") setPasswordPresent(false);
    return usernamePresent && passwordPresent;
  }

  const resetErrors = () => {
    setUsernamePresent(true);
    setPasswordPresent(true);
    setLoginErrors("")
  }

  return (
    <div>
      <h3>Log In</h3>
      <form onSubmit={handleSubmit}>
        {loginerrors !== "" && <SessionError error={loginerrors}/>}
        {!usernamePresent && <SessionError error="Username required" />}
        <input
          type="text"
          value={username}
          placeholder="Username"
          onChange={handleChange(setUsername)}
        />
        {!passwordPresent && <SessionError error="Password required" />}
        <input
          type="password"
          value={password}
          placeholder="Password"
          onChange={handleChange(setPassword)}
        />
        <input type='submit' />
      </form>

    </div>
  )
}

export default SessionForm;