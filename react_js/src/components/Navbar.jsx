import React from 'react'

const Navbar = () => {
  return (
    <nav className="navbar">
        <div className = "logo">Design AI</div>
        <ul className = "nav-links">
            <li><a href = "#hero">Home</a></li>
            <li><a href = "#features">Features</a></li>
            <li><a href = "#testimonials">Reviews</a></li>
        </ul>
    </nav>
  )
}

export default Navbar