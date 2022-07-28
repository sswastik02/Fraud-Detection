import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Link, useHistory } from "react-router-dom";
import "./CheckoutScreen.css";
import Navbar from "../components/Navbar";
import { useState } from "react";




function Checkout(){
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
                <input type="text" />
              </div>
              <div className="last-name">
                <label htmlFor="">Last Name</label>
                <input type="text" />
              </div>
            </div>
            <div className="row2">
              <div className="address">
                <label htmlFor="">Address</label>
                <input type="text" />
              </div>
              <div className="postal-code">
                <label htmlFor="">ZIP/Postal Code</label>
                <input type="text" />
              </div>
            </div>
            <div className="row3">
              <div className="city">
                <label htmlFor="">City</label>
                <input type="text" />
              </div>
              <div className="country">
                <div className="label">
                  <label htmlFor="">Country</label>
                </div>
                <div className="input">
                  <input type="text" />
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
                <input type="text" />
              </div>
              <div className="postal-code">
                <label htmlFor="">Card Number</label>
                <input type="text" />
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
              <button>Proceed to Payment </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
);

}


export default Checkout;