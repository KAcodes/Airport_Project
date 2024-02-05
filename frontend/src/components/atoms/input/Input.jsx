import { StyledInput } from './StyledInput';


const FormInput = ({
    name,
    value,
    color,
    onChange,
    placeholder,
    type,
    min,
    max
}) => {
    return <StyledInput 
                type={type} 
                color={color} 
                onChange={onChange} 
                name={name} 
                value={value}
                placeholder={placeholder}
                min={min}
                max={max}>
        </StyledInput>
}

export default FormInput;