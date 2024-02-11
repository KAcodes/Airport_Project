import {create} from 'zustand';

const useStore = create((set) => ({
  formValues: {
    search_location: '',
    city_id: 0,
    location: '',
    children: 0,
    adults: 2
  },
  setFormValue: (fieldName, value) => set((state) => ({ formValues: { ...state.formValues, [fieldName]: value } })),
  aiHolidayResponse: [],
  setAIHolidayResponse: (aiResponse) => set(() => ({ aiHolidayResponse: aiResponse})),
  hotelResponse: [],
  setHotelResponse: (hotels) => set(() => ({ hotelResponse: hotels})),

}));


const calendarStore = create((set) => ({
  selectedDates: ([new Date(), new Date()]),
  setSelectedDates: (dates) => set(() => ({ selectedDates: dates})),
}));

export {calendarStore, useStore} ;