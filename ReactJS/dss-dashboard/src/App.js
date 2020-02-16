import React from 'react';
import './App.css';
import Graph from './Graph'

function App() {
  return (
      <div className="App">
        <Graph param="Distance" title="Ramen"/>
        <Graph param="Weight" title="Sprite"/>
      </div>
  );
}

export default App;
