import React, {useState, useEffect} from 'react';
import classnames from 'classnames';

import * as calendar from './calendar';
import {useDispatch, useSelector} from 'react-redux'
import './index.css';
import {NoteActions, NoteCalendar} from '../../redux/actions'


export default function Calendar(props) {
    props = {
        date: new Date(),
        years: [2022],
        monthNames: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        // monthNames: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
        weekDayNames: ['Mo', 'Tu', 'We', 'Th' , 'Fr', 'Sa', 'Su'],
        // weekDayNames: ['Пн', 'Вт', 'Ср', 'Чт' , 'Пт', 'Сб', 'Вс'],
        onChange: Function.prototype
    };

    const [date, setDate] = useState(props.date)
    const [currentDate, setCurrentDate] = useState(new Date())
    const [selectedDate, setSelectedDate] = useState(new Date())
    const [status, setStatus] = useState(false)
    
    const dispatch = useDispatch()

    const NoteRed = useSelector(state => state.NoteReducer)
	const {notes} = NoteRed

    function checkData(num) {
        if (num.length == 1) {
            const numb = `0${num}`
            return numb
        } else {
            return num
        }
    }

    useEffect(() => {
        const month = checkData(String(selectedDate.getMonth() + 1))
        const day = checkData(String(selectedDate.getDate()))
        const year = String(selectedDate.getFullYear())
        dispatch(NoteActions({month: month, day: day, year: year}))
    }, [selectedDate])

    useEffect(() => {
        const month = checkData(String(selectedDate.getMonth() + 1))
        dispatch(NoteCalendar({month: month}))
    }, [status])
    

    const handlePrevMonthButtonClick = () => {
        const data = new Date(date.getFullYear(), date.getMonth() - 1);       
        setDate(data);
    };

    const handleNextMonthButtonClick = () => {
        const data = new Date(date.getFullYear(), date.getMonth() + 1);        
        setDate(data);
    };

    const handleDayClick = (date) => {
        setSelectedDate(date);
        props.onChange(selectedDate);
    };

        const { monthNames, weekDayNames } = props;
        const monthData = calendar.getMonthData(date.getFullYear(), date.getMonth());

        return (
            <div className="calendar">
                <header>
                    <button onClick={handlePrevMonthButtonClick}>{'<'}</button>
                    <div>
                        {monthNames.map((name, index) => (
                            <div>
                                <p>{index === date.getMonth() ? name : null}</p>
                            </div>
                        ))}
                    </div>
                        
                    <button onClick={handleNextMonthButtonClick}>{'>'}</button>
                </header>
                <table>
                    <thead>
                        <tr>
                            {weekDayNames.map(name =>
                                <th key={name}>{name}</th>    
                            )}
                        </tr>
                    </thead>
                    <tbody>
                        {monthData.map((week, index) =>
                            <tr key={index} className="week">
                                {week.map((day, index) => day ?
                                    <td
                                        key={index}
                                        className={classnames('day', {
                                            'today': calendar.areEqual(day, currentDate),
                                            'selected': calendar.areEqual(day, selectedDate)
                                        })}
                                        onClick={() => handleDayClick(day)}
                                        // onClick={() => console.log(day.getDay())}
                                    >
                                        <div className='dataStyle'>{day.getDate()}</div>
                                        {status === true? 
                                        (<div>
                                            <svg width="8" height="8" viewBox="0 0 8 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path fill-rule="evenodd" clip-rule="evenodd" d="M4 8C6.20914 8 8 6.20914 8 4C8 1.79086 6.20914 0 4 0C1.79086 0 0 1.79086 0 4C0 6.20914 1.79086 8 4 8Z" fill="#50E2C2"/>
                                            </svg>
                                        </div>):(<div></div>)}
                                    </td>
                                    :
                                    <td key={index} />
                                )}
                            </tr> 
                        )}
                    </tbody>
                </table>
            </div>
        );
}