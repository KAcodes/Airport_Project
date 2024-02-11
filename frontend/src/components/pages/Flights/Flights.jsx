import React, { useState } from "react";
import FlightTable from "../../organisms/FlightTable";
import ThreeSplitPage from "components/templates/ThreeSplitPage/ThreeSplitPage";
import { InputForm } from "./components/InputForm";

const Flights = () => {
  const [searchQuery, setSearchQuery] = useState("");
  const [FlightInfo, setFlightInfo] = useState(null);

  const fetchData = async (e) => {
    try {
      const response = await fetch(`/departures/${searchQuery}`);
      const data = await response.json();

      console.log(data);
      setFlightInfo(data);
    } catch (error) {
      console.error("Error fetching Flight information:", error);
    }
  };

  const handleSearch = (e) => {
    e.preventDefault();

    if (searchQuery) {
      fetchData();
    }
  };

  const firstColumn = (
    <InputForm
      handleSearch={handleSearch}
      searchQuery={searchQuery}
      setSearchQuery={setSearchQuery}
    />
  );
  const secondColumn = (
    <div>{FlightInfo && <FlightTable flight_data={FlightInfo} />}</div>
  );
  const thirdColumn = <p>Hello</p>;

  return (
    <ThreeSplitPage
      firstColumn={firstColumn}
      secondColumn={secondColumn}
      thirdColumn={thirdColumn}
    />
  );
};

export default Flights;
