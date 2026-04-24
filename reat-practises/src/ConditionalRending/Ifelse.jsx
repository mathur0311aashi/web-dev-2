import React from "react";

const Ifelse = () => {
    const isAgent = false;
    let msg;

    if(isAgent){
        msg = "Khatam..tata..goodbye"
    }
    else {
        msg = "Welcome to Karachi"
    }
    return (
        <>
            <div>Ifelse</div>
            <h1>{msg}</h1>
        </>
    );
};

export default Ifelse;
