import React from 'react'
import HolidayDiv from 'components/atoms/textbox/HolidayDiv'
import {useStore} from 'store/store'


const HolidayPlan = () => {

  const { aiHolidayResponse } = useStore();

  return (
    <>
        {aiHolidayResponse && aiHolidayResponse.map((idea) => 
            <HolidayDiv idea={idea} color="primary"/>
        )}
    </>
  )
}

export default HolidayPlan
