import styled from "styled-components";
import { colors } from "styles/theme/colors";

export const StyledButton = styled.button`
  display: flex;
  color: ${(props) =>
    props.color === "primary" ? colors.primary.text : colors.secondary.text};
  background: ${(props) =>
    props.color === "primary"
      ? colors.primary.backgroundColor
      : colors.secondary.backgroundColor};

  ${(props) =>
    props.hasBorder &&
    `
    border-width: 1px;
    border-radius: 5px;
    border-color: ${
      props.color === "primary" ? colors.primary.text : colors.secondary.text
    };`}

  margin: 2px;
  padding: 5px;
`;
