import React from "react";
import TabGroup from "../../molecules/TabGroup/TabGroup";
import { StyledNavBar } from "./StyledNavbar";
import { paths } from "components/routes/routes";

const Navbar = () => {
  const tabs = [
    {
      title: "Plan Holiday",
      routeTo: paths.home,
    },
    {
      title: "Departures",
      routeTo: paths.flights,
    },
    {
      title: "See Trends",
      routeTo: paths.trends,
    },
  ];

  return (
    <StyledNavBar>
      <TabGroup tabs={tabs} />
    </StyledNavBar>
  );
};

export default Navbar;
