import {useState} from "react";
import {Link} from "react-router-dom"
import {Button} from "@mui/material";
import axios from 'axios';

export default function Create(){
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [completed_by, setCompleted_by] = useState("");

    function handleSubmit(e){
        e.preventDefault();
        let formdata = new FormData();
        
        formdata.append("title", title)
        formdata.append("description", description)
        formdata.append("complete", false)
        formdata.append("completed_by", completed_by)
        console.log(formdata)
        const requestOptions = {
            method: 'POST',
            headers: { "Content-Type": "application/json"},  
        };

        axios.post("/todolist/todo", formdata, {headers: {'content-type': 'multipart/form-data'}}).then((response) => console.log(response.data));
    }
        
    return(
        <div>
            <div className="head">
                <p className='page_title'> Create a new To do item</p>
                <Button variant="contained" to = "/" component={Link} className="back_button">Back</Button>
            </div>
            <div className="form">
                <form>
                    <input type="text" className="form_input" placeholder="title" onChange={(e) => setTitle(e.target.value)}></input>
                    <input type="text" className="form_input" placeholder="description" onChange={(e) => setDescription(e.target.value)}></input>
                    <input type="date"  className="form_input" onChange={(e) => setCompleted_by(e.target.value)}></input>
                    <Button variant="contained" onClick={handleSubmit}>Create</Button>
                </form>

            </div>
        </div>
    )
}