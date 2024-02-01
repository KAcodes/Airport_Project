import React from 'react'
import FormInput from 'components/atoms/input/Input'
import Button from 'components/atoms/button/Button'
import DateRangePicker from '../Calendar/Calendar'
import {useStore} from 'store/store'


const InputGroup = () => {

    const { formValues, setFormValue, setAIHolidayResponse } = useStore();

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormValue(name, value);
    };

    const handleSubmit = async(e) => {

        e.preventDefault()
        const formData = formValues;
        console.log('Form Data:', formData);

        try {
            const response = await fetch(`/holiday_planner`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(formData),
            });
            const data = await response.json();
            console.log(data)
            setAIHolidayResponse(data)

        } catch (error) {
            console.error('Error fetching Flight information:', error);
        };
    

        // Clear form after submission if needed
        setFormValue('location', '');
        setFormValue('duration', '');
        setFormValue('age', '');
        setFormValue('gender', '');
    };


  return (
    <>
        <DateRangePicker/>
      <form onSubmit={handleSubmit} className="mx-auto">
        <label> Location: 
        <FormInput type="text" name="location" value={formValues.location} onChange={handleChange}/>
        </label>
       <label> Days: 
        <FormInput type="text" name="duration" value={formValues.duration} onChange={handleChange}/>
        </label>
       <label> Age: 
        <FormInput type="text" name="age" value={formValues.age} onChange={handleChange}/>
        </label>
        <label> Gender: 
        <FormInput type="text" name="gender" value={formValues.gender} onChange={handleChange}/>
        </label>
        <Button 
            title='Plan Me A Holiday' 
            color='primary'
            type="submit" 
        />
      </form>
    </>
  )
}

export default InputGroup
