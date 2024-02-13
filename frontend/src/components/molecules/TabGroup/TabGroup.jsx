import React from "react";
import TabButton from "components/atoms/tabButton/TabButton";
import { StyledTabGroup } from "./StyledTabGroup";
import { useNavigate, useLocation } from "react-router-dom";

const TabGroup = ({ tabs }) => {
  const navigate = useNavigate();

  const currentPath = useLocation().pathname;

  return (
    <StyledTabGroup>
      {tabs.map((tab) => (
        <TabButton
          key={tab.title}
          title={tab.title}
          color="secondary"
          onClick={() => navigate(tab.routeTo)}
          isactive={tab.routeTo == currentPath}
        />
      ))}
    </StyledTabGroup>
  );
};

export default TabGroup;
