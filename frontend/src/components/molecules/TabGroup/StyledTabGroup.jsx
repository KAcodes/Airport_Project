import styled from "styled-components";
import { colors } from "styles/theme/colors";

export const StyledTabGroup = styled.div`
  display: flex;
  justify-content: space-around;
  background: ${(props) =>
    props.color === "primary"
      ? colors.primary.backgroundColor
      : colors.secondary.backgroundColor};
  height: 50px;
  width: 100%;
`;
