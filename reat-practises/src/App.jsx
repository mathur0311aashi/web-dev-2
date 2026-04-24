import React from 'react'
import Ifelse from './ConditionalRending/Ifelse'
// import Ternary from './ConditionalRending/Ternary'
import UseStateone from './Hooks/UseStateone'
import Showhide from './Hooks/Showhide'
import Darklight from './Hooks/Darklight'
import Multicounter from './Hooks/Multicounter'
import UseEffect from './Hooks/UseEffect'

const App = () => {
  return (
    <>
      <div>App</div>
      <UseStateone/>
      <Ifelse />
      {/* <Ternary /> */}
      <Darklight/>
      <Showhide/>
      <Multicounter/>
      <UseEffect/>
    </>
  )
}

export default App