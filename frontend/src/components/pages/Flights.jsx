import React, { useState } from 'react';
import FlightTable from '../organisms/FlightTable';


const Flights = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [FlightInfo, setFlightInfo] = useState(null);

  const fetchData = async () => {
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
    if (searchQuery) {
      fetchData();
    }
  };

  return (
    <div>
      <h1>Flight Departure Information</h1>
      <input
        type="text"
        placeholder="Search for an Airport"
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Find Departures</button>

      {FlightInfo && (
        <div>
          <FlightTable flight_data={FlightInfo}/>
          {/* Display other Flight information as needed */}
        </div>
      )}
    </div>
  );
}

export default Flights
