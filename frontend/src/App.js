import logo from './logo.svg';
import './App.css';
import React from 'react';
import axios from 'axios';

function App() {
  const [counter, setCounter] = React.useState(0);
  const [loading, setLoading] = React.useState(false);

  React.useEffect(()=>{
    axios.get('http://localhost:8000/api/counter/1/')
      .then(response => {
        setCounter(response.data.count)
      })
  },[])

  const onCouting = (action) => {
    setLoading(true)
    const payload = {
      counter: counter,
      action: action
    }
    axios.post('http://localhost:8000/api/counter/1/', payload)
      .then(response => {
        setCounter(response.data.counter)
        setLoading(false)
      })
  }
  return (
    <div className="App">
      <header className="App-header">
        <div id="counter-container">
        <div>{counter}</div>
        <div id="btn-container">
        <button onClick={()=>onCouting(1)} disabled={loading}>Increment</button>
        <button onClick={()=>onCouting(0)} disabled={loading}>Decrement</button>
        </div>
        </div>
      </header>
    </div>
  );
}

export default App;
