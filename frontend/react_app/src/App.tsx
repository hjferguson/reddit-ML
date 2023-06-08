import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [title, setTitle] = useState("");
  const [prediction, setPrediction] = useState(""); // add this line

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/predict/', { title });
      console.log(response.data);
      setPrediction(response.data.prediction); // add this line
    } catch (error) {
      console.error("There was an error!", error);
    }
  }

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <label>
          Title:
          <input type="text" value={title} onChange={e => setTitle(e.target.value)} />
        </label>
        <input type="submit" value="Submit" />
      </form>
      <p>Prediction: {prediction}</p> 
    </div>
  );
}

export default App;
