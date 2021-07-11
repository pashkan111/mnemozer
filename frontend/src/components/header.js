import React from 'react'
import {Navbar, Nav, Form, FormControl, Button} from 'react-bootstrap'
import Window from './modal'

function Header() {
    return (
        <Navbar bg="light" expand="lg">
        <Navbar.Brand href="#home">Mnemozer</Navbar.Brand>
        <Window/>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
            </Nav>
        </Navbar.Collapse>
        </Navbar>
    )
}

export default Header
