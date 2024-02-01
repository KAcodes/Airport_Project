import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import { calendarStore } from 'store/store';

const DateRangePicker = () => {
  const {selectedDates, setSelectedDates} = calendarStore;

  const handleDateChange = (dates) => {
    setSelectedDates(dates);
  };

  return (
    <div>
      <h2>Select Date Range</h2>
      <Calendar
        onChange={handleDateChange}
        value={selectedDates}
        selectRange={true}
      />
      <div>
        <p>Selected Dates:</p>
        {/* <p>Start Date: {selectedDates[0].toLocaleDateString()}</p>
        <p>End Date: {selectedDates[1].toLocaleDateString()}</p> */}
      </div>
    </div>
  );
};

export default DateRangePicker;
