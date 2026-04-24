import React,{useState} from 'react'

const Darklight = () => {
    const[dark, setDark]= useState(false);
  return (
    <div style = {{ backgroundColor: dark ? "black" : "white", 
    color: dark ? "white" : "black" }}>
        <h1>{dark ? "Dark mode" : "Light mode"}</h1>
        <button onClick={() => setDark(!dark)}>Toggle theme</button>
    </div>
  )
}

export default Darklight