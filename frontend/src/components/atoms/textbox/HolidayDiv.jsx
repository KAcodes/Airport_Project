import { StyledText } from './StyledText';


const HolidayDiv = ({
    color,
    idea
}) => {
    return <StyledText 
                color={color} 
                >
            {idea}
        </StyledText>
}

export default HolidayDiv;