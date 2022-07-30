import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Link, useHistory } from "react-router-dom";
import "./AadharScreen.css";
import Navbar from "../components/Navbar";
import { useState } from "react";

function Aadhar() {
  const uid = localStorage.getItem("USER_ID");
  console.log(uid);
  const [firstname, setFirstName] = useState("");
  const [lastname, setLastName] = useState("");
  const [age, setAge] = useState("");

 
  const handleSubmit = async (e) => {
    e.preventDefault();

   

    await axios
      .put(`http://localhost:5000/api/aadharinfo/${uid}`, {
        firstname: firstname,
        lastname: lastname,
        age: age,
       
      })
      .then((res) => {
        console.log(res);
        
      })

      .catch((err) => console.log(err));
  };
  return (
    <div>
      <div className="container">
        <div className="form">
          <form>
            <div className="title">
              <h2>Student Discount</h2>
            </div>
            <div className="shipping">
              <h3>Upload Aadhar Card to Verify your Age</h3>
              <div className="row1">
                <div className="first-name">
                  <label htmlFor="">First Name</label>
                  <input type="text" onChange={(e) => {
                      setFirstName(e.target.value);
                    }}
                    value={firstname}/>
                </div>
                <div className="last-name">
                  <label htmlFor="">Last Name</label>
                  <input type="text"   onChange={(e) => {
                      setLastName(e.target.value);
                    }}/>
                </div>
              </div>

              <div className="row3">
                <div className="info">
                  <div className="label">
                    <label for="file">
                      Upload a Aadhar Pdf:{" "}
                      <input type="file" name="file" />
                    </label>
                    <label for="age">
                      Input you age (years):
                      <input type="text"   onChange={(e) => {
                      setAge(e.target.value);
                    }} />
                    </label>
                  </div>
                </div>
              </div>
            </div>

            <div className="row5">
              <div className="button">
                <button  onClick={handleSubmit}>Proceed to Verify </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Aadhar;
