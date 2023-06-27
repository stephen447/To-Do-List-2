import {useState, useEffect} from "react";
import {Link} from "react-router-dom"
import {Button, Checkbox} from "@mui/material";
import axios from 'axios';

export default function Todolist(){
    const[listitems, setListitems] = useState("")

    function list(){
        
        axios.get("/todolist/todo")
        .then((response) => setListitems(response.data));
    
    }

    const handleCheckbox = (event, id, complete)=>{
        event.preventDefault()
        const requestOptions = {
            method: 'PUT',
            headers: { "Content-Type": "application/json"},
          };
          console.log(complete)
        fetch("/todolist/todo?id="+id+"&complete="+complete, requestOptions)
          .then((response) => response.json())
          .then((data) => console.log(data));

    }

    const handleDelete = (event, id)=>{
        event.preventDefault()
        const requestOptions = {
            method: 'DELETE',
            headers: { "Content-Type": "application/json"},
          };
        fetch("/todolist/todo?id="+id, requestOptions)
          .then((response) => response.json())
          .then((data) => console.log(data));

    }
    useEffect(() => {list()});
    return(
        <div>
            <div className="head">
                <p className="page_title">To Do list</p>
                <Button variant="contained" to = "/" component={Link} className="back_button">Back</Button>
            </div>
            {Object.values(listitems).map(value =>
            <div className="todoitem">
                <div className="row">
                        <p className="title">{value.title}</p>
                        <Checkbox className="checkbox" checked={value.complete} onChange={(event)=>handleCheckbox(event, value.id, !value.complete)}></Checkbox>
                        <Button onClick={(event)=>handleDelete(event, value.id)}>Delete</Button>
                </div>
                <div>
                    <p className="description">{value.description}</p>
                    <p className="description">Complete by: {value.completed_by}</p>
                </div>
                
            </div>
            )}
        </div>
        
    )
    
}