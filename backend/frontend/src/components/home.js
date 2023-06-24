import React, { Component } from "react"
import Button from "@mui/material/Button"
import {BrowserRouter as Router, Route, Routes, Link} from "react-router-dom"
import Todolist from "./todolist";
import Create from "./create";
import Login from "./login";

class Home extends Component {
    constructor(props){
        super(props);
    }

    renderhome(){
        return(
            <div>
                <div>
                    <h1>To Do List</h1>
                </div>
                <div>
                    <Button variant="contained" className="home_button" to="/todolist" component={Link}>View</Button>
                    <Button variant="contained" className="home_button" to="/create" component={Link}>Create</Button>
                    <Button variant="contained" className="home_button" to="/login" component={Link}>Login</Button>
                </div>
            </div>
        )
    }

    render(){
        return(
            <Router>
                <Routes>
                    <Route path="" element = {this.renderhome()}/>
                    <Route path="todolist" element = {<Todolist/>}/>
                    <Route path="create" element = {<Create/>}/>
                    <Route path="login" element = {<Login/>}/>
                </Routes>
            </Router>
        )
    }
}
export default Home