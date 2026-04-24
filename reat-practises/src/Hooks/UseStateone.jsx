import React, { useState } from 'react'

const UseStateone = () => {
// the only top level for hooks used
    const [count, setCount] =  useState(0) // 0 is the initial value of count
// this is the hooks syntax in which we actually have to use 2 variables atleast bocz 1 holds the value and the otehr has toohe hooks 
// hooks variable setcount update the current state manage ke liye use hota hai
// use state se wo actually work krta h
// then coems the definetion of array ki it cn store actually the same value
    function increase(){
        setCount(count + 1)
        // current state ko kaise update krna h  is done by setCount
    }

    function decrease(){
        setCount(count - 1)
    }

    function reset(){
        setCount(0)
    }
  return (
    <>
    <div>UseStateone</div>
    <h1>Count:{count}</h1>
// react me variable render ke liye{} isme likhte h  
    <button onClick = {increase}>Click</button>
    <button onClick = {decrease}>Click</button>
    <button onClick = {reset}>Click</button>
    </>
)
}

export default UseStateone