// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.28;

contract DataMarketplace {
    error DataMarketplace__NotAIAgent();

    struct Data {
        string description;
        address user;
    }

    uint32 public latestDataNum;
    address public aiAgent;
    address public owner;
    string public dataNeeded;
    Data[] public aiTrainingData;

    event NewDataCreated(uint32 indexed dataIndex, Data data);
    event AIAgentResponded(uint32 indexed dataIndex, Data data, address aiAgent, bool isValid);

    modifier isOwner() {
        require(msg.sender == owner, "Not the Owner");
        _;
    }

    constructor(address newAIAgent) {
        aiAgent = newAIAgent;
        owner = msg.sender;
    }

    function createNewData(
        string memory description
    ) external returns (Data memory) {
        Data memory newData;
        newData.description = description;
        newData.user = msg.sender;

        emit NewDataCreated(latestDataNum, newData);
        latestDataNum = latestDataNum + 1;

        return newData;
    }

    function respondToNewData(
        Data calldata data,
        uint32 referenceDataIndex,
        bool isValid
    ) external {
        if (msg.sender != aiAgent) {
            revert DataMarketplace__NotAIAgent();
        }

        if (isValid) aiTrainingData.push(Data(data.description, data.user));

        emit AIAgentResponded(referenceDataIndex, data, msg.sender, isValid);
    }

    function updateDataNeeded(string memory newData) public {
        dataNeeded = newData;
    }

    function getDataNeeded() public view returns(string memory){
       return dataNeeded;
    }

    function getAllData() public view returns(Data[] memory){
       return aiTrainingData;
    }
}
