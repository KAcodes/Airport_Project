import { StyledTabButton } from "./StyledTabButton";

const TabButton = ({ title, color, onClick, isactive }) => {
  console.log(isactive);
  return (
    <StyledTabButton color={color} onClick={onClick} isactive={isactive}>
      {title}
    </StyledTabButton>
  );
};

export default TabButton;
