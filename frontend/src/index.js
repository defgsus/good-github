import React from "react"
import ReactDOM from "react-dom";
import App from "./comps/App";


window.addEventListener('DOMContentLoaded', (event) => {
    const app = document.getElementById("app");
    ReactDOM.render(<App />, app);
});
