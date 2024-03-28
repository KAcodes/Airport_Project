import React from "react";
import { useStore } from "store/store";
import Hotel from "components/molecules/Hotel/Hotel";

const HotelResults = () => {
  const { hotelResponse } = useStore();

  const hotels = hotelResponse.api_response;
  return (
    <div>
      {hotels &&
        hotels.map((hotel, index) => (
          <Hotel hotel={hotel} key={index}/>
        ))}
    </div>
  );
};

export default HotelResults;
