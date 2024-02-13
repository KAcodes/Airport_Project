import styled from "styled-components";
import { colors } from "styles/theme/colors";

export const StyledTabButton = styled.button`
  display: flex;
  color: ${(props) =>
    props.color === "primary" ? colors.primary.text : colors.secondary.text};
  background: ${(props) =>
    props.color === "primary"
      ? colors.primary.backgroundColor
      : colors.secondary.backgroundColor};

  ${(props) =>
    props.isactive &&
    `
    border-bottom-style: solid;
    border-width: 0px 0px 4px 0px;
    border-color: ${
      props.color === "primary" ? colors.primary.text : colors.secondary.text
    };
    `}

  margin: 2px;
  padding: 5px;
`;
