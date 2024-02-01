import React, { useState } from 'react';
import FlightTable from '../organisms/FlightTable';
import FormInput from 'components/atoms/input/Input';
import Button from 'components/atoms/button/Button';


const Flights = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [FlightInfo, setFlightInfo] = useState(null);

  const fetchData = async (e) => {
    try {

      const response = await fetch(`/departures/${searchQuery}`);
      const data = await response.json();

      console.log(data)
      setFlightInfo(data)
    } catch (error) {
      console.error('Error fetching Flight information:', error);
    }
  };


  const handleSearch = (e) => {
    e.preventDefault();

    if (searchQuery) {
      fetchData();
    }
  };

  return (
    <div className='flex flex-row h-screen'>
      <div className='bg-blue-400 w-1/5'>
        <form onSubmit={handleSearch}>
          <label> Airport IATA: 
            <FormInput type="text" placeholder={"Search for an Airport"} name="airport" value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)}/>
          </label>
          <Button 
            title='Find Departures' 
            color='primary'
            type="submit" 
          />
        </form>
      </div>
      <div className='bg-green-400 w-3/5'>
          {FlightInfo && (
          <FlightTable flight_data={FlightInfo}/>
          )}
      </div>
      <div className='bg-yellow-400 w-1/5'>
          <p>Hello</p>
      </div>
    </div>
  );
}

export default Flights
