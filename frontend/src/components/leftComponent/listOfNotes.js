import React from 'react'
import Note from './note'
import {useDispatch, useSelector} from 'react-redux'

function ListOfNotes() {
    const [element, setElement] = React.useState([])

    const NoteRed = useSelector(state => state.NoteReducer)
	const {notes} = NoteRed

	React.useEffect(() => {
		console.log(notes)
        setElement(notes)
	}, [notes])

    return (
        element.map(item => (
        <div>
            {/* <Note name={element.name} date={element.date} time={element.time} done={element.done} />  */}
            <Note name={item.name} date={item.date} time={item.time} done={item.done} /> 
        </div>
        ))
    )
}

export default ListOfNotes
