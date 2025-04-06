import React, { useState, useEffect } from 'react';

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

export default MyComponent;
