import React from 'react'

const FlightTable = ({flight_data}) => {
  return (
    
    <table className="table-auto">
        <thead>
            <tr>
            <th>Flight Number</th>
            <th>Destination</th>
            <th>Airport IATA</th>
            <th>Country</th>
            <th>Expected Departure</th>
            <th>Duration</th>
            <th>Expected Arrival</th>
            </tr>
        </thead>
        <tbody>
            {flight_data && (
                flight_data.map((flight, flight_id) => (
                    <tr key={flight_id}>
                        <td>{flight["flight_iata"]}</td>
                        <td>{flight["destination_airport"]}</td>
                        <td>{flight["arr_iata"]}</td>
                        <td>{flight["destination_country"]}</td>
                        <td>{flight["dep_time_utc"]}</td>
                        <td>{flight["duration"]}</td>
                        <td>{flight["arr_time_utc"]}</td>
                    </tr>
                ))
            )}
        </tbody>
    </table>
    
  )
}

export default FlightTable
