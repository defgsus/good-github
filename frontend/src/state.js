import {useCallback, useReducer} from "react";
import PropTypes from 'prop-types';

import state_context from "./context";


const DEFAULT_STATE = {
    error: null,
    message_index: null,
    message_map: {},
    date: null,
    object_snapshots: null,
};



export function reducer(state, action) {
    //console.log("ACTION", action);
    //console.log("OLD STATE", state);
    state = reducer_impl(state, action);
    //console.log("NEw STATE", state);
    return state;
}

function reducer_impl(state, action) {
    if (action.type.endsWith("_FAILED")) {
        state = {
            ...state,
            error: action.event
        };
    }

    switch (action.type) {
        case "SET_DATE":
            return {
                ...state,
                date: action.date,
            };

        case "FETCH_MESSAGE_INDEX_SUCCESS":
            prepare_message_index(action.data);
            return {
                ...state,
                message_index: action.data,
            };

        case "FETCH_MESSAGE_FILE_STARTED":
            return {
                ...state,
                message_map: {
                    ...state.message_map,
                    [action.args.date]: {},
                },
            };

        case "FETCH_MESSAGE_FILE_SUCCESS": {
            const messages = parse_message_file(action.data);
            return {
                ...state,
                message_map: {
                    ...state.message_map,
                    [action.args.date]: messages,
                },
            };
        }
        default:
            return state;
    }
}


const StateProvider = ({children}) => {
    const [state, dispatch] = useReducer(reducer, DEFAULT_STATE);

    const request = useCallback(
        (action_name, method, url, args) => {
            const req = new XMLHttpRequest();
            req.open(method, url);
            req.onload = e => {
                let data;
                try {
                    data = JSON.parse(req.response);
                }
                catch (e) {
                    data = req.response;
                }
                dispatch({type: `${action_name}_SUCCESS`, event: e, data, args});
            };
            req.onerror = e => {
                dispatch({type: `${action_name}_FAILED`, event: e, args});
            };
            req.onprogress = e => {
                dispatch({type: `${action_name}_PROGRESS`, progress: e.loaded / e.total * 100}, args);
            };
            dispatch({type: `${action_name}_STARTED`, method, url, args});
            req.send();
        },
        [dispatch]
    );

    return (
        <state_context.Provider value={{...state, request, dispatch}}>
            {children}
        </state_context.Provider>
    );
};

StateProvider.propTypes = {
    children: PropTypes.element.isRequired,
};

export default StateProvider;


const weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];


function prepare_message_index(index) {
    const rows = [];
    let row = [];
    let last_year = 0;
    let last_day = 0;
    let max_messages = 1;
    for (const m of index.index) {
        max_messages = Math.max(max_messages, m.num_messages);
        m.available = true;
        m.date_str = m.date;
        m.date = new Date(m.date + "T00:00:00Z");
        m.weekday = m.date.getDay();
        m.weekday_str = weekdays[m.weekday];
        m.title = `${m.num_messages} messages on ${m.weekday_str} ${m.date_str}`;
        m.year = m.date.getUTCFullYear();

        if (last_year !== m.year) {
            if (row.length)
                rows.push(row);
            rows.push(`${m.year}`);
            row = [];
        }

        if (m.weekday === 0){// || Math.abs(m.date.getDay() - last_day) > 7) {
            if (row.length)
                rows.push(row);
            row = [];
        }
        else {
            for (let i = row.length; i < m.weekday; ++i)
                row.push({weekday: i, title: "no data"});
        }
        last_day = m.date.getDay();
        last_year = m.year;

        row.push(m);
    }
    if (row.length)
        rows.push(row);

    for (const m of index.index) {
        m.color_level = m.num_messages
            ? Math.min(6, (m.num_messages / max_messages * 7).toFixed())
            : 0;
    }

    for (const row of rows) {
        if (typeof row === "object" && row.length < 7) {
            for (let i = row.length; i < 7; ++i)
                row.push({weekday: i, title: "no data"});
        }
    }

    index.rows = rows;
}

function parse_message_file(markdown) {
    //markdown = markdown.slice(markdown.indexOf("\n"), markdown.length-53);
    return {
        "markdown": markdown
    };
}