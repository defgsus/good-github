import React, { useCallback, useContext, useEffect } from "react"
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import state_context from "../context"


const GoodMessages = () => {

    const {
        message_index,
        message_map,
        date,
        request,
        dispatch,
    } = useContext(state_context);

    useEffect(() => {
        request("FETCH_MESSAGE_INDEX", "GET", "good-messages/index.json");
    }, []);

    useEffect(() => {
        if (message_index?.index && !message_map[date]) {
            if (!date)
                dispatch({type: "SET_DATE", date: message_index.index[message_index.index.length - 1].date_str});
            for (const m of message_index.index) {
                if (m.date_str === date) {
                    const url = `good-messages/${date.slice(0, 4)}/${date}.md`;
                    request("FETCH_MESSAGE_FILE", "GET", url, {date});
                    break;
                }
            }
        }
    }, [date, message_index, message_map]);

    return (
        <div className={"good-messages"}>
            <div className={"grid-x nowrap"}>

                <CalendarSidebar
                    index={message_index}
                    dispatch={dispatch}
                    date={date}
                />

                <div className={"messages grow"}>
                    {message_map[date] && message_map[date].markdown
                        ? (
                            <ReactMarkdown
                                linkTarget={"_blank"}
                                remarkPlugins={[remarkGfm]}
                                components={{
                                    a({href, children, node, ...props}) {
                                        // replace the relative markdown links with click handler
                                        let match = href.match(/^(\d\d\d\d)-(\d\d)-(\d\d)\.md$/);
                                        if (!match)
                                            match = href.match(/^\.\.\/\d\d\d\d\/(\d\d\d\d)-(\d\d)-(\d\d)\.md$/);
                                        if (match) {
                                            const match_date = match.slice(1, 4).join("-");
                                            return <a
                                                onClick={() => dispatch({type: "SET_DATE", date: match_date})}
                                                className={"clickable"}
                                                title={`go to ${match_date}`}
                                            >{children}</a>;
                                        }
                                        return <a href={href} {...props}>{children}</a>;
                                    }
                                }}
                            >
                                {message_map[date].markdown}
                            </ReactMarkdown>
                        )
                        : <h1>{date}</h1>
                    }
                </div>
            </div>
        </div>
    );
};

export default GoodMessages;


const CalendarSidebar = ({index, date, dispatch}) => {
    if (!index?.rows)
        return null;
    //console.log(index);
    return (
        <div className={"calendar-sidebar"}>
            {index.rows.map((row, i) => {
                if (typeof row === "string")
                    return <div key={i} className={"year grow"}>{row}</div>;
                return (
                    <div className={"week-row grid-x nowrap"} key={i}>
                        {row.map((m, j) => (
                            <div
                                key={j}
                                className={
                                    "day" + (m.available ? " available" : "")
                                    + (m.color_level ? ` level-${m.color_level}` : "")
                                    + (m.date_str === date ? " selected" : "")
                                }
                                title={m.title}
                                onClick={() => {
                                    if (m.date_str)
                                        dispatch({type: "SET_DATE", date: m.date_str});
                                }}
                            />
                        ))}
                    </div>
                );
            })}
        </div>
    )
};