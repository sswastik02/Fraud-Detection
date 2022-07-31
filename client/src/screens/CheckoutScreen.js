import React, { Component } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Link, useHistory } from "react-router-dom";
import "./CheckoutScreen.css";
import Navbar from "../components/Navbar";
import { useState } from "react";
import useEth from "../contexts/EthContext/useEth";
import axios from "axios";


  const read = async (a,b,c,i,d,e) => {
    console.log("architlallllllll")
   // const value = 
     await contract.methods.addTransaction(a,b,c,i,d,e).send({ from: accounts[0] });
    //setValue(value);
  };

 

  // const read = async (a,b,c,i,d,e) => {
  //   console.log("helloooo")
  //  const value = 
  //    await contract.methods.addTransaction(a,b,c,i,d,e).send({ from: accounts[0] });
  //   setValue(value);
  // };
 


  const uid = localStorage.getItem("USER_ID");
  
  
  console.log(uid);
  const [firstname, setFirstName] = useState("");
  const [lastname, setLastName] = useState("");
  const [address, setAddress] = useState("");

  const [zip, setZip] = useState("");
  const [city, setCity] = useState("");
  const [country, setCountry] = useState("");
  const [cardholdername, setCardholderName] = useState("");
  const [card, setCard] = useState("");

  const handleSubmit = async (e) => {
    
    e.preventDefault();

   console.log('submit')

    await axios
      .put(`http://localhost:5000/api/userinfo/${uid}`, {
        firstname: firstname,
        lastname: lastname,
        address: address,
        zip: zip,
        city: city,
        country: country,
        cardholdername: cardholdername,
        card: card,
      })
      .then((res) => {
        console.log(res);
        if(res.data ==true ) {
          // alert('frauddddddddddddd')
          // read("ARCHIT","wfeff","ffff",2,"effefe","cweefef");
        }
         else {
          console.log('read function called')
          read(res.firstname,"wfeff","ffff",2,"effefe","cweefef");
         }
       
        
      })

      .catch((err) => console.log(err));
  };
  
  return (
    <div>
      <div className="container">
        <div className="form">
          <form>
            <div className="title">
              <h2>Shipping &amp; Billing</h2>
            </div>
            <div className="shipping">
              <h3>Shipping Address</h3>
              <div className="row1">
                <div className="first-name">
                  <label htmlFor="">First Name</label>
                  <input
                    type="text"
                    onChange={(e) => {
                      setFirstName(e.target.value);
                    }}
                    value={firstname}
                  />
                </div>
                <div className="last-name">
                  <label htmlFor="">Last Name</label>
                  <input
                    type="text"
                    onChange={(e) => {
                      setLastName(e.target.value);
                    }}
                    value={lastname}
                  />
                </div>
              </div>
              <div className="row2">
                <div className="address">
                  <label htmlFor="">Address</label>
                  <input
                    type="text"
                    onChange={(e) => {
                      setAddress(e.target.value);
                    }}
                    value={address}
                  />
                </div>
                <div className="postal-code">
                  <label htmlFor="">ZIP/Postal Code</label>
                  <input
                    type="text"
                    onChange={(e) => {
                      setZip(e.target.value);
                    }}
                    value={zip}
                  />
                </div>
              </div>
              <div className="row3">
                <div className="city">
                  <label htmlFor="">City</label>
                  <input
                    type="text"
                    onChange={(e) => {
                      setCity(e.target.value);
                    }}
                    value={city}
                  />
                </div>
                <div className="country">
                  <div className="label">
                    <label htmlFor="">Country</label>
                  </div>
                  <div className="input">
                    <input
                      type="text"
                      onChange={(e) => {
                        setCountry(e.target.value);
                      }}
                      value={country}
                    />
                  </div>
                </div>
              </div>
            </div>
            <br />
            <br />
            <div className="billing">
              <h3>Payment Details</h3>
              <div className="row1"></div>

              <div className="row3">
                <div className="address">
                  <label htmlFor="">Card Holder</label>
                  <input
                    type="text"
                    onChange={(e) => {
                      setCardholderName(e.target.value);
                    }}
                    value={cardholdername}
                  />
                </div>
                <div className="postal-code">
                  <label htmlFor="">Card Number</label>
                  <input
                    type="text"
                    onChange={(e) => {
                      setCard(e.target.value);
                    }}
                    value={card}
                  />
                </div>
              </div>
              <div className="row4">
                <div className="city">
                  <label htmlFor="">CVV</label>
                  <input type="text" />
                </div>
                <div className="country">
                  <div className="label">
                    <label htmlFor="">Expiration Date (MM/YY)</label>
                  </div>
                  <div className="input">
                    <input type="text" />
                  </div>
                </div>
              </div>
            </div>
            <div className="row5">
              <div className="button">
                <button onClick={handleSubmit}>Proceed to Payment </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
);
   

                