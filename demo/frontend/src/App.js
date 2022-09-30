//Imports
//Styles
import logo from './banner.png';
import './App.css';

//unused attempt to have live location
import Loc from "./Location";
//Importing State and effect management
import React,{useState,useEffect} from 'react';

//Main body
function App() {
  //Establishes variables for Blog post list
  const [data,setData]=useState([]);
  //Establishes Current Astronauts in space variables
  const [currAstros,setCurrAstros]=useState([]);
  //Esttablishes current prominent post on page
  const [currPost,setCurrPost]=useState([]);
  console.log("Variables established")

//Retreive api data functions
//Gets information for blog list
  const getData=()=>{
        fetch('http://127.0.0.1:8000/api/list/?format=json'  ,{headers : { 'Content-Type': 'application/json','Accept': 'application/json'}})
         .then(function(response){
          //console.log(response)
          return response.json();})
          .then(function(myJson) {
            //console.log(myJson);
           setData(myJson)
          })};
  //Gets latest blog post
   const getTopPost=()=>{
          fetch('http://localhost:8000/api/latest/?format=json',{headers : {'Content-Type': 'application/json', 'Accept': 'application/json'} } )
         .then(function(response){
          //console.log(response) 
          return response.json();})
          .then(function(myJson) {
          //console.log(myJson);
           setCurrPost(myJson)
          })};
        //Gets current astronauts in space
    const getCurrAstros=()=>{
          fetch('http://localhost:8000/api/astroCurr/?format=json',{headers : {'Content-Type': 'application/json', 'Accept': 'application/json'} } )
          .then(function(response){
            //console.log(response) 
          return response.json();})
          .then(function(myJson) {
          //console.log(myJson);
          setCurrAstros(myJson)
            })
            };  
    //Gets specific post, assigns to curr post        
    const getCurrPost=(props)=>{
      try{
      fetch('http://localhost:8000/api/detail/'+props+'/?format=json',{headers : {'Content-Type': 'application/json', 'Accept': 'application/json'} } )
 .then(function(response){
  //console.log("I am here!",response) 
  return response.json();})
  .then(function(myJson) {
  //console.log(myJson);
   setCurrPost(myJson)
  })}
  catch(err){
    console.log("Error in retrieving post data",err)
  };


    }

    //On launch gather data
      useEffect(()=>{
            
             getData();
            
             getCurrAstros();

             getTopPost();
             
             console.log("loaded initail data");
              },[])
    

  //sets form to default           
const initialFormData = Object.freeze({
  postID: 0,
});
//Adds form data retrieval functionality
const SearchForm = () => {
  const [formData, updateFormData] = React.useState(initialFormData);
//backend adding form field stuff to variables
  const doChange = (e) => {

    //Prevents a negative number being submitted
    if (formData.postID<0){
      return null;
    };
    updateFormData({
      ...formData,

      [e.target.name]: e.target.value.trim()
    });
  };
//submits data to get current post
  const doSubmit = (e) => {
    e.preventDefault()
    //console.log(formData);
    //Provides an alert to noitify the user of a wrongfull submission
    if (formData.postID<=-1){
      alert("Blog IDs Start at 1")
      return null;
    }
    //fixing my messup
    if (formData.postID===2){
      alert("I accidentally deleted 2. So now enjoy this pop up(Try again)")
      return null;
    }
    console.log("form submitted");

   

    getCurrPost(formData.postID);
    

    
};
  

//Output form(field) to screen
  return (
    <>
      <label>
        BlogID:
        <input name="postID" onChange={doChange} type="number" />
      </label>
    
      <button onClick={doSubmit}>Submit</button>
    </>
  );
};// 

//<Loc />
//main page
   return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        
        
  <table><tbody><tr><td> 
    <div className="App Blog-Posts">
        
       {  <div><h1 className="postMain">{currPost.postTitle}</h1><p className="postMain">{currPost.postBulk}</p><img src={currPost.postPic} alt="Top Post image"  className="blog-img" ></img></div> }

       
       <SearchForm />
       <button onClick={() => getTopPost()}>Reset</button>
       {data && data.length>0 && data.map((item)=><div key={item.postID}><h1>{item.postTitle}</h1><img src={item.postPic} className="blog-img" alt={"BlogID: "+item.postID}></img><p><button onClick={() => getCurrPost(item.postID)} type="submit">{"BlogID: "+item.postID}</button></p></div>)}
       

       </div> </td>
    <td>
    <div className="App">
    <table><tbody>

    <p>Currently in space is: </p>
     {
       
       currAstros && currAstros.length>0 && currAstros.map((item)=><div key={item.astorID}><tr><td className='spacePeeps'><h3><b>{item.astroName}</b></h3> <p>{item.astroCraft}</p></td></tr></div>)
     }

    
     </tbody></table>
    </div></td>
    </tr>
    </tbody></table> 
       
      </header>
    </div>
  );
    };
//exports to index.js
export default App;
