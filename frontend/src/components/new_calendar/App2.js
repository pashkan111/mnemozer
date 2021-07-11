import React, {useState, useEffect} from 'react';
import Calendar from './index';

export default function App2() {
	const [date, setDate] = useState(null)
    
	// function handleDateChange (data) {
	// 	setDate(data);
	// }
		return (
			<div>
				{date && date.toLocaleDateString()}
				<Calendar
					onChange={(data) => setDate(data)}
				/>
			</div>
		);
	}