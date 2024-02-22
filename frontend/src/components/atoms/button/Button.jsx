import { StyledButton } from "./StyledButton";

const Button = ({ title, icon, color, onClick, hasBorder }) => {
  return (
    <StyledButton
      role={"button"}
      color={color}
      onClick={onClick}
      hasBorder={hasBorder}
    >
      {icon && icon}
      {title}
    </StyledButton>
  );
};

export default Button;
