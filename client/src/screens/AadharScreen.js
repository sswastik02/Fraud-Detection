import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Link, useHistory } from "react-router-dom";
import "./AadharScreen.css";
import Navbar from "../components/Navbar";
import { useState } from "react";

function Aadhar() {
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
                  <input type="text" />
                </div>
                <div className="last-name">
                  <label htmlFor="">Last Name</label>
                  <input type="text" />
                </div>
              </div>

              <div className="row3">
                <div className="info">
                  <div className="label">
                    <label for="file">
                      Upload a profile picture:{" "}
                      <input type="file" name="file" />
                    </label>
                    <label for="age">
                      Input you age (years):
                      <input type="text" />
                    </label>
                  </div>
                </div>
              </div>
            </div>

            <div className="row5">
              <div className="button">
                <button>Proceed to Verify </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Aadhar;
