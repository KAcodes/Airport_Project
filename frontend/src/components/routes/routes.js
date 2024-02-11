import Flights from "components/pages/Flights/Flights";
import Travel from "components/pages/Travel/Travel";
import Trends from "components/pages/Trends/Trends";
import { useRoutes } from "react-router-dom";

export const paths = {
  home: "/",
  flights: "/flights",
  trends: "/trends",
};

export const Pages = () => {
  return useRoutes([
    { path: paths.home, element: <Travel /> },
    { path: paths.flights, element: <Flights /> },
    { path: paths.trends, element: <Trends /> },
  ]);
};
