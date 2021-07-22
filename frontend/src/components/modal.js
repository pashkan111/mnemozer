import React from 'react'
import {Button, Modal, Form, FormGroup, FormLabel, FormControl, Row, Col } from 'react-bootstrap'



function Window() {
    const [show, setShow] = React.useState(false);
    
    const [Name, setName] = React.useState('');
    const [description, setDescription] = React.useState('');
    const [day, setDay] = React.useState('');
    const [month, setMonth] = React.useState('');
    const [year, setYear] = React.useState('');
    const [notification, setNotification] = React.useState('');

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    function handlerSubmit() {
        
    }
  
    return (
      <>
        <Button variant="light" onClick={handleShow}>
        <svg width="47" height="47" viewBox="0 0 47 47" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M23.5 47C36.4787 47 47 36.4787 47 23.5C47 10.5213 36.4787 0 23.5 0C10.5213 0 0 10.5213 0 23.5C0 36.4787 10.5213 47 23.5 47Z" fill="#4D3088"/>
        </svg>
        </Button>
  
        <Modal show={show} onHide={handleClose} animation={false}>
          <Modal.Header>
              <div style={{position: 'relative', left: '100px'}}>
                <Modal.Title>Create New Tasks</Modal.Title>
              </div>

          </Modal.Header>
          <Modal.Body>

          <div>
              <Row className>
                  <Col>
                    <Form onSubmit={handlerSubmit}>
                    {/* <FormGroup controlId='email'> */}
                        <FormLabel>Topic</FormLabel>
                        <FormControl
                            value={Name}
                            placeholder={'Write Topic'}
                            onChange={(e) => setName(e.target.value)}
                        />
                    {/* </FormGroup> */}
                    {/* <FormGroup controlId='email'> */}
                        <FormLabel>Description</FormLabel>
                        <FormControl
                            value={description}
                            placeholder={'Write Description'}
                            onChange={(e) => setDescription(e.target.value)}
                        />
                    {/* </FormGroup> */}
                  <Row className='col-md-12'>
                    <Col className='col-md-4'>
                    {/* <FormGroup controlId='email'> */}
                        <FormLabel>day</FormLabel>
                        <FormControl
                            type='number'
                            value={day}
                            placeholder={'04'}
                            onChange={(e) => setDay(e.target.value)}
                        />
                    {/* </FormGroup> */}
                    </Col>
                    {/* <FormGroup contpmrolId='email'> */}
                    <Col className='col-md-4'>
                        <FormLabel>Month</FormLabel>
                        <FormControl
                            type="number"
                            max={2}
                            value={month}
                            placeholder={'12'}
                            onChange={(e) => setMonth(e.target.value)}
                        />
                      </Col>
                    {/* </FormGroup> */}
                    {/* <FormGroup contpmrolId='email'> */}
                    <Col className='col-md-4'>
                        <FormLabel>Year</FormLabel>
                        <FormControl
                            type='number'
                            value={year}
                            placeholder={'2021'}
                            onChange={(e) => setYear(e.target.value)}
                        />
                      </Col>
                    {/* </FormGroup> */}
                  </Row>
                    {/* <FormGroup contpmrolId='email'> */}
                        <FormLabel>Notification</FormLabel>
                        <FormControl
                            value={notification}
                            placeholder={'10 minutes before'}
                            onChange={(e) => setNotification(e.target.value)}
                        />
                    {/* </FormGroup> */}
                    </Form>
                  </Col>
              </Row>
          </div>

          </Modal.Body>
          <Modal.Footer>
        <button type="button" class="btn btn-secondary">Secondary</button>
          </Modal.Footer>
        </Modal>
      </>
    );
  }
  
export default Window
