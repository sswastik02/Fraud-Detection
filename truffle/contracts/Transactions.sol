// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract Transactions {
  uint public sno=0;

 struct Transaction{
  uint _sno;
  string _buyerID;
  string _buyername;
  string _sellername;
  uint _amount;
  string _productID;
  string _buyerEmail;
  uint256 _time;
 }

 mapping(uint=> Transaction) public transaction;

  function addTransaction(string memory _buyerID, string memory _buyername, string memory _sellername, uint _amount, string memory _productID, string memory _buyerEmail) public{
    sno++;
    transaction[sno] = Transaction(sno,_buyerID,_buyername,_sellername,_amount,_productID,_buyerEmail, block.timestamp);
  }
}
