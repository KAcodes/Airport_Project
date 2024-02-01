import React from 'react';
import './App.css';
import { BrowserRouter as Router} from 'react-router-dom';
import Header from './components/organisms/Header';
import Navbar from './components/organisms/Navbar';
import { Pages } from 'components/routes/routes';


const App = () => {
  
  return (
    <>
        <Header/>
        <div className='grid bg-red-600'>
          <Router>
            <Navbar/>
              <Pages />
          </Router>
        </div>
    </>
  );
};

export default App
