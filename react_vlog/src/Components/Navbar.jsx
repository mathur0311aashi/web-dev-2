import React, { useState, useEffect} from 'react'
import { Link } from 'react-router-dom' 
import Data from '../Data'

const Navbar = () => {
  const [menuOpen, setMenuOpen] = useState(false)
    const [scrolled, setScrolled] = useState(false)
    const location = useLocation()

    useEffect(() => {
        const handleScroll = () => setScrolled(window.scrollY > 20)
        window.addEventListener('scroll', handleScroll)
        return () => window.removeEventListener('scroll', handleScroll)
    }, [])

    useEffect(() => {
        setMenuOpen(false)
    }, [location])

    const navLinks = [
        { to: '/',           label: 'Home',       icon: '⌂' },
        { to: '/bollywood',  label: 'Bollywood',  icon: '✦' },
        { to: '/hollywood',  label: 'Hollywood',  icon: '◈' },
        { to: '/tech',       label: 'Technology', icon: '⬡' },
        { to: '/fitness',    label: 'Fitness',    icon: '◎' },
        { to: '/food',       label: 'Food',       icon: '❋' },
    ]
  return (
    
    <div>
        <Link to = "/">Home</Link>
        <Link to = "/bollywood">Bollywood</Link>
        <Link to = "/hoolywood">Hollywood</Link>
        <Link to = "/technology">Technology</Link>
        <Link to = "/fitness">Fitness</Link>
        <Link to = "/food">Food</Link></div>
  )
}

export default Navbar