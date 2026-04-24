import React from 'react'
import Data from '../Data'
import { Link } from 'react-router-dom'

const Bollywood = () => {

  const bollywoodData = Data.filter(item => item.category === 'Bollywood')
  console.log(bollywoodData)
  return (
    <>

      <div>Bollywood</div>
      {bollywoodData.map((bollydata) => (
        <>
          <Link to={`/post/${bollydata.id}`}>
            <h1>{bollydata.title}</h1>
            <img src={bollydata.img_url} />
          </Link>
        </>
      ))}
    </>
  )
}

export default Bollywood