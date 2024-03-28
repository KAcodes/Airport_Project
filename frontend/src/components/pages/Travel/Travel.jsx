import SideBar from "./components/SideBar";
import React from "react";
import HolidayResults from "components/pages/Travel/components/HolidayResults";
import ThreeSplitPage from "components/templates/ThreeSplitPage/ThreeSplitPage";
import HotelResults from "./components/HotelResults";

const Travel = () => {
  const firstColumn = <SideBar />;
  const secondColumn = <HolidayResults />;
  const thirdColumn = <HotelResults/>;

  return (
    <ThreeSplitPage
      firstColumn={firstColumn}
      secondColumn={secondColumn}
      thirdColumn={thirdColumn}
    />
  );
};

export default Travel;
