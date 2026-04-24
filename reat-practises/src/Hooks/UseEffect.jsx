import React, { useState } from 'react'

const UseEffect = () => {
    const [count, setCount] = useState(0)
    const { count, setCount } = useState // 0 is the initial value of count
        //   return (

        <div> UseEffect </div>
        <h1>Count1:</h1>
        <button onClick = {() => setCount(count + 1)}></button>
        <h1>Count2 :</h1>


}

export default UseEffect