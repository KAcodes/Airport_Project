import React, { useState, useEffect } from 'react';
import FlightTable from './FlightTable';


const Flights = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [FlightInfo, setFlightInfo] = useState(null);

  const fetchData = async () => {
      try {
        // Make a request to your Flask API endpoint with the search query
        const response = await fetch(`/departures/${searchQuery}`);
        const data = await response.json();
        
        // Update state with the retrieved Flight information
        console.log(data)
        setFlightInfo(data)
        // setFlightInfo(result);
      } catch (error) {
        console.error('Error fetching Flight information:', error);
        // Handle errors as needed
      }
    };


  const handleSearch = (e) => {
    if (searchQuery) {
      fetchData();
    }
  };

  return (
    <div>
      <h1>Flight Information</h1>
      <input
        type="text"
        placeholder="Search for an Airport"
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Fetch Data</button>

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
