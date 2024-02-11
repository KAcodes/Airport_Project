import SideBar from "./components/SideBar";
import React from "react";
import HolidayResults from "components/pages/Travel/components/HolidayResults";
import ThreeSplitPage from "components/templates/ThreeSplitPage/ThreeSplitPage";

const Travel = () => {
  const firstColumn = <SideBar />;
  const secondColumn = <HolidayResults />;
  const thirdColumn = <p>Hello</p>;

  return (
    <ThreeSplitPage
      firstColumn={firstColumn}
      secondColumn={secondColumn}
      thirdColumn={thirdColumn}
    />
  );
};

export default Travel;
