import styled from "styled-components";
import { colors } from "styles/theme/colors";

export const StyledHeader = styled.div`
  display: flex;
  position: fixed;
  color: ${(props) =>
    props.color === "primary" ? colors.primary.text : colors.secondary.text};
  background: ${(props) =>
    props.color === "primary"
      ? colors.primary.backgroundColor
      : colors.secondary.backgroundColor};

  padding: 25px;
  width: 100%;
  height: 75px;
`;
