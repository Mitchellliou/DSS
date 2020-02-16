import React from 'react';
import './App.css';
import Graph from './Graph'
// import { db } from './firebase'
// import firebase from './firebase'

// db.collection("sampleData")
// .get()
// .then(querySnapshot => {
//   const data = querySnapshot.docs.map(doc => doc.data());
//   console.log(data); // array of cities objects
// });


function App() {
  return (
    <div className="App">
      <Graph/>
    </div>
  );
}

export default App;
