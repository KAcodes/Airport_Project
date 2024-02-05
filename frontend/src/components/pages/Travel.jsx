import SideBar from 'components/organisms/SideBar'
import React from 'react'
import HolidayResults from 'components/organisms/HolidayResults'

const Travel = () => {

  return (
    <div className='flex flex-row h-screen'>
      <div className='bg-blue-400 w-1/5'>
          <SideBar/>
      </div>
      <div className='bg-green-400 w-3/5'>
          <p>Holiday Suggestions</p>
          <HolidayResults/>
      </div>
      <div className='bg-yellow-400 w-1/5'>
          <p>Hello</p>
      </div>
    </div>
  )
}

export default Travel
