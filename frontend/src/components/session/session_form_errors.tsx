import React from 'react';

interface Props {
  error: string
}

const SessionError = ({ error }: Props) => {
  return (
    <div className='session-error'>
      {error}
    </div>
  )
}

export default SessionError;