import { StyledButton } from './StyledButton';


const Button = ({
    title,
    icon,
    color,
    onClick,
}) => {
    return <StyledButton color={color} onClick={onClick}>
            {icon && icon}
            {title}
        </StyledButton>
}

export default Button;