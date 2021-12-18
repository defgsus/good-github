import React, { useCallback, useContext, useEffect } from "react";
import state_context from "../context";
import GoodMessages from "./GoodMessages";


const FrontPage = () => {

    const {
        error,
        dispatch,
    } = useContext(state_context);

    return (
        <div className={"front"}>

            <div className={"grid-x margin-right"}>
                <div><div className={"inline"}>good github</div></div>
                <div className={"grow"}/>
                <div>
                    <a href={"https://github.com/defgsus/good-github"} target={"_blank"}>github</a>
                </div>
            </div>

            {error ? <div className={"error"}>{error}</div> : null}

            <GoodMessages/>

        </div>
    );
};

export default FrontPage;

