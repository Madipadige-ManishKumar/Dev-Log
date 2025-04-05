import './mycss.css';
import React from 'react'; 
import ReactDOM from 'react-dom/client';

import { useState,useEffect } from 'react';

function MyForm() {
  const [name, setName] = useState("");

  return (
    <>
    <form>
      <label>Enter your name:
        <input
          type="text" 
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

      </label>
      <input type="submit" value="submit"/>
    </form>
    <span style={{fontSize:'50px',backgroundColor:'cyan',color:'red'}}>{name} </span>
    </>
    // <p> {name} </p>
  );
}

class Car extends React.Component  {
  render () {
    return (
    <>
      <ul style={{ listStyleType: 'none', margin: '20px', padding: '0' }}>
        <li style={{ color: this.props.c1, fontWeight: 'bold' }}>Item 1</li>
        <li style={{ color: this.c2 }}>Item 2</li>
        <li style={{ color: this.c3 }}>Item 3</li>
      </ul>

      <div
        style={{
          width: '200px',
          height: '100px',
          backgroundColor: 'lightblue',
          borderRadius: '10px',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        <span style={{ color: 'darkblue', fontSize: '16px' }}>Styled Div</span>
      </div>
    </>
    )
  }
}

function mybutton1()
{
  return (
    <button onclick="shoot()">CLick Here </button>
  );
}

function shoot() {
  alert(" aa hello bhai");
} 

function  Fav_color()
{
  const [color,setcolor]=useState("red");
  return (
    <>
    <h2 style={{backgroundColor:color}}> My color {color} </h2>
    <button  onClick={() =>{
      setcolor("blue");
    }} >Blue </button>


<button  onClick={() =>{
     setcolor("yellow")
    }} >Yellow </button>

<button  onClick={() =>{
      setcolor("pink");
    }} >pink </button>
    </>
  );
}

function MyComponent() {
  const [message, setMessage] = useState("Hello");

  // This useEffect runs after the component is mounted
  useEffect(() => {
    console.log("Component has mounted!");
    
    // Simulating data fetching or side effect
    setMessage("Hello, World!");  // Update state after mounting
  }, []); // Runs only once after initial render

  // Function to handle button click
  const handleClick = () => {
    setMessage("You clicked the button!");
  };

  return (
    <div>
      <p>{message}</p>
      <button onClick={handleClick}>Click me!</button>
    </div>
  );
}



function App() {
  const handleClick = () => {
    alert('Hello bhai');
  };

  return (
    <>
      <span className="myh1">This is the updated react application</span>
      <Car c1={"red"}  c2={"black"} c3={"white"} />
      {/* <mybutton1 /> */}
      <button onClick={shoot}>CLick Here </button>
      <MyForm />

      <Fav_color/>
      <MyComponent />
    </>
  );
}


export default App;