import React from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import Data from '../Data'

const Details = () => {
    //dyanmically change that is why in {}
    const { id } = useParams()
    const navigate = useNavigate()
    const post = Data.find((item) => item.id === parseInt(id))
    return (
        <>
            <div>Details</div>
            <button onClick={() => navigate(-1)}>Go Back</button>

            <>
                <h1>{post.title}</h1>
                <img src={post.img_url} />
                <p>{post.description}</p>
            </>

        </>
    )
}

export default Details