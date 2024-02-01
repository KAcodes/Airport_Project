import styled from 'styled-components';
import { colors } from 'components/theme/colors';

export const StyledInput = styled.input`
    display: flex;
    color: ${props => (props.color === 'primary' ? colors.primary.text : colors.secondary.text)};
    background: ${props => (props.color === 'primary' ? colors.primary.backgroundColor : colors.secondary.backgroundColor)};
    
    border-width: 1px;
    border-radius: 5px;
    border-color: ${props => (props.color === 'primary' ? colors.primary.text : colors.secondary.text)};

    margin: 2px;
    padding: 5px;
`;

