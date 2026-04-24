import React from 'react'
import Child from './Child'

const Parent = () => {
    const fullname = "Hamza Ali Mazari";
    function Alert (){
        alert("Hosla Endhan Badla")
    }

return {
    <>
    <div>Parent</div>
    <h1>Rendered in Parent <comp:>fullname</comp:></h1>
    <Child name = {fullname} alert={alert}/>
    </>
}

// function \() {
//   return (
//     <div>\</div>
//   )
// }

export default 