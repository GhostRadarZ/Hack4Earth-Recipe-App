import { useState } from 'react'
// import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Homepage from './Components/Homepage';
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Homepage />
      
    </>
  )
}

export default App
