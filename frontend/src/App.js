import { useState, useEffect } from "react";
import axios from "axios"

function App() {
  const [todoList, setTodoList] = useState([])

  useEffect(() => {
    axios
    .get("/api/todos/")
    .then((res) => {
      console.log(res.data)
      setTodoList(res.data)
    })
    .catch((err) => console.log(err))
  },[])
  
  return (
    <div>
      <p> {todoList.map((e) => {
        return(
          <div>
            <p> {e.title} </p>
            <p> {e.description} </p>
          </div>
        )
      })} </p>
    </div>
  );
}

export default App;
