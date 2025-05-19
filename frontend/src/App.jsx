import React from "react"

import HomePage from "./pages/HomePage.jsx"
import {Routes, Route} from "react-router-dom"
import DetailsRestaurantPage from "./pages/DetailsRestaurantPage.jsx"

function App() {


  return (
 
      <Routes>
        <Route path="/" element={<HomePage/>} />
        <Route path="/restaurant" element={<DetailsRestaurantPage/>}/>
      </Routes>  

    
    
    
  )
}

export default App
