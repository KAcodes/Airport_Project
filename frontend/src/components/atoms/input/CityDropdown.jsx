// CityDropdown.js
import React, { useState, useEffect } from 'react';

const CityDropdown = () => {
  const [inputValue, setInputValue] = useState('');
  const [filteredCities, setFilteredCities] = useState([]);

  useEffect(() => {
    const filterCities = async() => {
        const response = await fetch(`/cities/${inputValue}`)
        const data = await response.json();
        setFilteredCities(data)
    }
    if (inputValue.trim() !== '') {
      filterCities()
    } else {
      setFilteredCities([]);
    }
  }, [inputValue]);

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleSelectCity = (selectedCity) => {
    setInputValue(selectedCity);
    setFilteredCities([]); // Clear the dropdown
  };

  return (
    <div>
      <input
        type="text"
        value={inputValue}
        onChange={handleInputChange}
        placeholder="Type a city..."
      />
      {filteredCities.length > 0 && (
        <ul>
          {filteredCities.map((city) => (
            <li key={city} onClick={() => handleSelectCity(city)}>
              {city}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default CityDropdown;
