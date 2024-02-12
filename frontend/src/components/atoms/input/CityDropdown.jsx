import React, { useState, useEffect } from 'react';
import {useStore} from 'store/store'


const CityDropdown = () => {

  const { formValues, setFormValue } = useStore();
  const [filteredCities, setFilteredCities] = useState([]);

  useEffect(() => {

    if (formValues.search_location.length >= 4)  {
      const filterCities = async() => {
        const response = await fetch(`/cities/${formValues.search_location}`)
        const data = await response.json();
        setFilteredCities(data)
    }
    if (formValues.search_location.trim() !== '') {
      filterCities()
    } else {
      setFilteredCities([]);
    }
    }

  }, [formValues.search_location]);


  const handleSelectCity = (selectedCity) => {
    setFormValue("location", `${selectedCity.city_name}, ${selectedCity.country_name}`);
    setFormValue("city_id", selectedCity.city_id);
    setFormValue("search_location", "");
    setFilteredCities([]);
  };

  return (
    <>
      {filteredCities.length > 0 && (
        <ul className='px-4 py-2 bg-blue-100 space-y-2 data-dropdown-toggle="dropdown"'>
          {filteredCities.map((city) => (
            <li className='hover:bg-gray-100 cursor-pointer' key={city.city_id} onClick={() => handleSelectCity(city)}>
              {city.city_name}, {city.country_name}
            </li>
          ))}
        </ul>
      )}
    </>
  );
};

export default CityDropdown;
