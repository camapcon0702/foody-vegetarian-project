import React from "react"

import HomePage from "./pages/HomePage.jsx"
import {Routes, Route} from "react-router-dom"
import DetailsRestaurantPage from "./pages/DetailsRestaurantPage.jsx"
import ListRestaurant from "./components/ListRestaurant/ListRestaurant.jsx"
import ResultSearchPage from "./pages/ResultSearchPage.jsx"

function App() {


  return (
 
      <Routes>
        <Route path="/" element={<HomePage/>} />
        <Route path="/restaurant" element={<DetailsRestaurantPage/>}/>
        <Route path="/search" element={<ResultSearchPage/>}/>
      </Routes>  

    
    
    
  )
}

export default App
