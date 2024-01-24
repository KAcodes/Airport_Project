import './App.css';

import React, { useState, useEffect } from 'react';
import Flights from './components/Flights';
import Travel from './components/Travel';


const App = () => {
  
  

  return (
    <>
      <div>
        <Flights/>
        <Travel/>
      </div>
    </>
  );
};

export default App

