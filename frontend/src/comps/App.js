import React from "react";
import StateProvider from "../state";
import FrontPage from "./FrontPage";


const App = () => {

    try {
        return (
            <StateProvider>
                <FrontPage/>
            </StateProvider>
        );
    }
    catch (e) {
        return (
            <div className={"error"}>{`${e}`}</div>
        );
    }
};

export default App;
