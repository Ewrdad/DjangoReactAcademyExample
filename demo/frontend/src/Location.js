import React,{useState,useEffect} from 'react';

function Loc(){
    //Establishes variables for Blog post list
    const [locStuff,setLocStuff] =useState([]);
    const [things,setThings]=useState([]);
    const getLocStuff=()=>{
        fetch('http://localhost:8000/api/iss/?format=json'  ,{headers : { 'Content-Type': 'application/json','Accept': 'application/json'}})
         .then(function(response){
          //console.log(response);
          return response.json();})
          .then(function(myJson) {
            //console.log(myJson);
           setLocStuff(myJson);
          })
        return locStuff};

          useEffect(()=>{
            
            getLocStuff();
            
            
             },[]);

       
    const latLong = locStuff.iss_position;
    //const lat = latLong.latitude;
          //{data.iss_position.latitude}
        // {data.iss_position.latitude}

          return ( <div><p>{latLong}</p><h1>Lat:</h1> <h2>long:</h2></div>)

};

//exports to app.js
export default Loc;
