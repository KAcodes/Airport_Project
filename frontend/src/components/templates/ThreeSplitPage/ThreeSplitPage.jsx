import {
  QuarterColumn,
  HalfColumn,
  StyledThreeSplitPage,
} from "./StyledThreeSplitPage";

const ThreeSplitPage = ({ firstColumn, secondColumn, thirdColumn }) => {
  return (
    <StyledThreeSplitPage>
      <QuarterColumn>{firstColumn} </QuarterColumn>
      <HalfColumn>{secondColumn} </HalfColumn>
      <QuarterColumn>{thirdColumn} </QuarterColumn>
    </StyledThreeSplitPage>
  );
};

export default ThreeSplitPage;
