import React from "react";
import FormInput from "components/atoms/input/Input";
import Button from "components/atoms/button/Button";
import DateRangePicker from "components/molecules/Calendar/Calendar";
import { useStore, calendarStore } from "store/store";
import CityDropdown from "components/atoms/input/CityDropdown";

const SideBar = () => {

  const { formValues, setFormValue, setAIHolidayResponse, setHotelResponse } =
    useStore();
  const { selectedDates } = calendarStore();
  const dept_date = selectedDates[0].toLocaleDateString();
  const return_date = selectedDates[1].toLocaleDateString();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormValue(name, value);
  };

  const handleSubmit = async (e) => {
  
    e.preventDefault();
    const formData = formValues;
    const newData = {
      ...formData,
      dept_date: dept_date,
      return_date: return_date,
    };

    try {
      const response = await fetch(`/holiday_planner`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newData),
      });
      const data = await response.json();
      console.log(data);
      setAIHolidayResponse(data["response"]);
    } catch (error) {
      console.error("Error fetching Flight information:", error);
    }

    try {
      const response = await fetch("/holiday_planner/hotels", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newData),
      });
      const data2 = await response.json();
      console.log(data2);
      setHotelResponse(data2);
    } catch (error) {
      console.error("Error fetching Hotels:", error);
    }

    setFormValue("search_location", "");
    setFormValue("age", "");
  };

  return (
    <>
      <DateRangePicker />
      <form onSubmit={handleSubmit} className="mx-auto">
        <label>
          {" "}
          Location: {formValues.location}
          <FormInput
            type="text"
            name="search_location"
            value={formValues.search_location}
            onChange={handleChange}
            placeholder={"e.g. Town, City, Country"}
          />
          <CityDropdown />
        </label>
        <label>
          Adults (16+ years):{" "}
          <FormInput
            type="number"
            name="adults"
            value={formValues.adults}
            onChange={handleChange}
            min={0}
          />
        </label>
        <label>
          {" "}
          Children (0-16 years):
          <FormInput
            type="number"
            name="children"
            value={formValues.children}
            onChange={handleChange}
            min={0}
          />
        </label>
        <Button title="Plan Me A Holiday" color="primary" type="submit" />
      </form>
    </>
  );
};

export default SideBar;
