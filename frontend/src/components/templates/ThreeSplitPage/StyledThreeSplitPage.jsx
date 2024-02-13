import styled from "styled-components";
import { colors } from "styles/theme/colors";

export const QuarterColumn = styled.div`
  width: 25%;
  height: 100%;
  background: ${colors.uniform.lightBackgroundColor};
  padding: 20px;
`;

export const HalfColumn = styled.div`
  width: 50%;
  height: 100%;
  padding: 20px;
`;

export const StyledThreeSplitPage = styled.div`
  display: flex;
  justify-content: center;
  height: 100%;
  padding-top: 125px;
`;
