import styled from "styled-components";
import { colors } from "styles/theme/colors";

export const StyledText = styled.div`
    display: flex;
    width: 80%
    color: ${(props) =>
      props.color === "primary" ? colors.primary.text : colors.secondary.text};
    background: ${(props) =>
      props.color === "primary"
        ? colors.primary.backgroundColor
        : colors.secondary.backgroundColor};
    
    border-width: 1px;
    border-radius: 5px;
    border-color: ${(props) =>
      props.color === "primary" ? colors.primary.text : colors.secondary.text};

    margin-top: 2px;
    margin-bottom: 2px;

    padding: 5px;
`;
