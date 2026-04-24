// // rafce se aaya h syntax se code likhne ke liye
// import React from 'react'

// import Navbar from '@eslint/js'

// const App = () => {
//   return (
//     <div>App</div>
//   nav
//   )
// }

// export default App

import Navbar from "./components/Navbar";
import HeroSection from "./components/HeroSection";
import Features from "./components/Features";
import Testimionals from "./components/Testimonials";
import Footer from "./components/Footer";
import Parent from "./Props/Parent";

function App() {
  return (
    <> 
    
    <Parent>
      <Navbar />
      <HeroSection />
      <Features />
      <Testimionals />
      <Footer />
      <div>App</div>
      <h1>App</h1>
    
    </Parent>
    </>
  );
}

export default App;
