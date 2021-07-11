import React from 'react'
import ListOfNotes from './listOfNotes'
import Buttons from '../buttons'

function LeftComponent() {
    return (
        <div>
            <Buttons/>
        <div style={{backgroundColor: '#665B7C', height: '100vh', width: '493px'}}>
            <ListOfNotes/>
        </div>
        </div>
    )
}

export default LeftComponent
