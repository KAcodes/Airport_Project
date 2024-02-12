import React from "react";

const Hotel = ({ hotel }) => {
  return (
    <div className="p-2 space-y-3">
      <h2>{hotel.name}</h2>
      <img src={hotel.media?.url} alt="pic" />
      <h3>Stars = {hotel.starRating}</h3>
      <h4>
        Minimum Price = <em>{hotel.ratesSummary.minPrice}</em>{" "}
        {hotel.ratesSummary.minCurrencyCode} per night
      </h4>
    </div>
  );
};

export default Hotel;
