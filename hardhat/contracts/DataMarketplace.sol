// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.28;

contract DataMarketplace {
    error DataMarketplace__NotAIAgent();

    uint32 public latestDataNum;

    struct Data {
        string description;
        address user;
    }

    address public aiAgent;

    Data[] public aiTrainingData;

    event NewDataCreated(uint32 indexed dataIndex, Data data);
    event AIAgentResponded(uint32 indexed dataIndex, Data data, address aiAgent, bool isValid);

    constructor(address newAIAgent) {
        aiAgent = newAIAgent;
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
}
