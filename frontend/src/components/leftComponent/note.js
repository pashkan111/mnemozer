import React from 'react'
import './styles.css'
import {Container, Row, Col} from 'react-bootstrap'

function Note(props) {
    const {name, date, time, done} = props
    
    return (
        <div className='note'>
            <div style={{marginTop: '17px'}}>
                <Row className='col-md-12'>
                    <Col md={3}>
                        <p style={{display: 'flex'}}>{name}</p>
                    </Col>
                    <Col md={3}>
                        <p style={{display: 'flex'}}>{date}</p>
                    </Col>
                    <Col md={3}>
                        <p style={{display: 'flex'}}>{time}</p>
                    </Col>
                    <Col md={3}>
                        <p className='deleteItem'>
                            <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect width="22" height="22" fill="#FF5C5C"/>
                            </svg>
                        </p>
                    </Col>
                </Row>
            </div>

        </div>
    )
}

export default Note
