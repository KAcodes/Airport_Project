import {create} from 'zustand';

const useStore = create((set) => ({
  formValues: {
    location: '',
    duration: '',
    age: '',
    gender: ''
  },
  setFormValue: (fieldName, value) => set((state) => ({ formValues: { ...state.formValues, [fieldName]: value } })),
  aiHolidayResponse: [],
  setAIHolidayResponse: (aiResponse) => set(() => ({ aiHolidayResponse: aiResponse}))
}));

const calendarStore = create((set) => ({
  selectedDates: ([new Date(), new Date()]),
  setSelectedDates: (dates) => set(() => ({ selectedDates: dates})),
  
}));

export {useStore, calendarStore};