import React from 'react'
import ReactDOM from 'react-dom'

function App(props) {
  return (
    <div>
      <h1>Todo List</h1>
    <ul>
      {props.data.map((row, index) => (
        <li key={index.toString()}>{row}</li>
      ))}
    </ul>
  </div>
  )
}

ReactDOM.render(
  <App {...window.props} />,
  document.getElementById("app")
)
