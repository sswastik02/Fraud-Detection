import { useState } from "react";
import useEth from "../contexts/EthContext/useEth";

function ContractBtns({ setValue }) {
  const { state: { contract, accounts } } = useEth();
  const [inputValue, setInputValue] = useState("");

  const handleInputChange = e => {
    if (/^\d+$|^$/.test(e.target.value)) {
      setInputValue(e.target.value);
    }
  };

  const read = async () => {
    console.log("helloooo")
   // const value = 
     await contract.methods.addTransaction("hellooo","hellooo","hellooo",20,"dwf","ffw").send({ from: accounts[0] });
    //setValue(value);
  };

//   const write = async e => {
//     console.log(helloooo)
//     await await contract.methods.addTransaction("helloooo","helloooo","helloooo",20,"dwf","ffw").call({ from: accounts[0] });
//   };

  return (
    <div className="btns">

      <button onClick={read}>
        read()
      </button>

      {/* <div onClick={write} className="input-btn">
        write(<input
          type="text"
          placeholder="uint"
          value={inputValue}
          onChange={handleInputChange}
        />)
      </div> */}

    </div>
  );
}

export default ContractBtns;
