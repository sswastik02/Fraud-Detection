// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract TodoList {
  uint public count=0;

 struct Todo{
  string info;
  uint sno;
 }

 mapping(uint=> Todo) public todos;

  function addTodo(string memory _info) public{
    count++;
    todos[count] = Todo(_info,count);
  }
}
