import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Link,useHistory} from "react-router-dom";
import "./AadharScreen.css";
import Navbar from "../components/Navbar";
import { useState } from "react";
import axios from "axios";




function Aadhar() {
    const navigate = useHistory();

    const [fileInputState, setFileInputState] = useState('');
    const [previewSource, setPreviewSource] = useState('');
    const [selectedFile, setSelectedFile] = useState();
   
    const uid = localStorage.getItem("USER_ID");
  console.log(uid);
    const handleFileInputChange = (e) => {
        const file = e.target.files[0];
        previewFile(file);
        setSelectedFile(file);
        setFileInputState(e.target.value);
    };

    const previewFile = (file) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onloadend = () => {
            setPreviewSource(reader.result);
        };
    };

    const handleSubmitFile = (e) => {
        e.preventDefault();
        if (!selectedFile) return;
        const reader = new FileReader();
        reader.readAsDataURL(selectedFile);
        reader.onloadend = () => {
            uploadImage(reader.result);
        };
        reader.onerror = () => {
            console.error('AHHHHHHHH!!');
           
        };
    };

    const uploadImage = async (base64EncodedImage) => {
            // console.log(base64EncodedImage)
        try {
            axios.put(`http://localhost:5000/api/aadharinfo/${uid}`, {
            
                body: JSON.stringify({ data: base64EncodedImage }),
                headers: { 'Content-Type': 'application/json' },
            }).then((res) => {
                // let res = JSON.parse(resp)
                console.log(res.data.document);
                setFileInputState('');
               
                if(res.data.document == false) alert('Fradulent identity proof detected')
                else{
                    alert('valid id proof')
                    // window.location.replace("/")
                }
              })
             

            
        } catch (err) {
            console.error(err);
           
        }
    };
  
    return (
        < div className="aadharscreen">
            <h1 className="title">Upload an Image</h1>
          
            <form onSubmit={handleSubmitFile} className="form">
                <input
                    id="fileInput"
                    type="file"
                    name="file"
                    onChange={handleFileInputChange}
                    value={fileInputState}
                    className="form-input"
                />
                <button className="btn" type="submit">
                    Submit
                </button>
            </form>
            {previewSource && (
                <img
                    src={previewSource}
                    alt="chosen"
                    style={{ height: '300px' }}
                />
            )}
        </div>
    );
}

export default Aadhar;
