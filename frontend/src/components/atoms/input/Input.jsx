import { StyledInput } from './StyledInput';


const FormInput = ({
    name,
    value,
    color,
    onChange,
    placeholder
}) => {
    return <StyledInput color={color} onChange={onChange} name={name} value={value} placeholder={placeholder}>
        </StyledInput>
}

export default FormInput;