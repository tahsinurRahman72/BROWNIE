// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SetIndividual{
    // address owner;

    // modifier onlyOwner(){
    //     require(msg.sender==owner);
    //     _;
    // }
    // mapping(uint => Individuals) public individual;
    Individuals[] public individual;
    uint256 public individualCount;

    struct Individuals{
        // uint id;
        int256 variety; //alternating column name for type
        uint256 amount;
        uint256 oldbalanceOrg;
        uint256 newbalanceOrig;
        uint256 oldbalanceDest;
        uint256 newbalanceDest;
        bool isFraud;
    }

    // constructor(){
    //     owner == msg.sender;
    // }

    function commitIndividual(int256 _variety, uint256 _amount, uint256 _oldbalanceOrg, 
                           uint256 _newbalanceOrig, uint256 _oldbalanceDest, 
                           uint256 _newbalanceDest, bool _isFraud) 
                           public{        
        // individual[individualCount] = Individuals(individualCount,_variety, _amount, _oldbalanceOrg, _newbalanceOrig, _oldbalanceDest, _newbalanceDest, _isFraud);                      
        individual.push(Individuals(_variety, _amount, _oldbalanceOrg, _newbalanceOrig, _oldbalanceDest, _newbalanceDest, _isFraud));
        individualCount+=1;
    }
    function retrieve() public view returns(uint256) {
        return individualCount;
    }

 }