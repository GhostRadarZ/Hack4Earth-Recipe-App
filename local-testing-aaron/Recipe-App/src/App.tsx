//import { useState } from 'react'
//import reactLogo from './assets/react.svg'
//import viteLogo from '/vite.svg'
import Title from './Title.tsx';
import ListGroup from './componenets/ListGroup.tsx';
import './App.css'
import Button from './componenets/Button.tsx';
import { useState } from 'react';
import ListGroupClose from './componenets/ListGroupClose.tsx';

function App() {
  //const [count, setCount] = useState(0)
  let ingredients = ["Bannana","Potato","Tomato"]
  let recipies = ["Salad","Pizza","Pasta"]

  const [ingredientsVisible,setIngredientsVisiblity] = useState(false);

  return (
    <>
        <div>
        <Title></Title>
        </div>
        <div>
        <Button onClick={() => setIngredientsVisiblity(true)}>Show Ingredients</Button> 
        <Button onClick={() => setIngredientsVisiblity(false)}> Show Recipies </Button> 
        </div>
        {ingredientsVisible && <ListGroupClose items={ingredients} onClose={() => console.log("close button pressed")}></ListGroupClose>}
        {!ingredientsVisible && <ListGroup items={recipies}></ListGroup>}
    </>
  )
}

export default App


/*
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
*/