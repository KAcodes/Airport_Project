import React, { useState, useEffect } from 'react';


const Flights = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [FlightInfo, setFlightInfo] = useState(null);

  const fetchData = async () => {
      try {
        // Make a request to your Flask API endpoint with the search query
        const response = await fetch(`/countries/${searchQuery}`);
        const data = await response.json();
        const result = data["results"]
        // Update state with the retrieved Flight information
        setFlightInfo(result);
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
        placeholder="Search for a Flight"
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Fetch Data</button>

      {FlightInfo && (
        <div>
          <h2>{FlightInfo}</h2>
          {/* Display other Flight information as needed */}
        </div>
      )}
    </div>
  );
}

export default Flights
