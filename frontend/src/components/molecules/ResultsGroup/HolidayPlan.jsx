import React from 'react'
import HolidayDiv from 'components/atoms/textbox/HolidayDiv'
import {useStore} from 'store/store'


const HolidayPlan = () => {

  const { aiHolidayResponse } = useStore();

  return (
    <>
        {aiHolidayResponse && aiHolidayResponse.map((idea, key) => 
            <HolidayDiv key={key} idea={idea} color="primary"/>
        )}
    </>
  )
}

export default HolidayPlan
