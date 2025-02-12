#!/usr/bin/env python
import sys
import warnings
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
import os

from datetime import datetime

from filframe_ai.crew import FilframeAi

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    
    try:
        FilframeAi().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        FilframeAi().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        FilframeAi().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        FilframeAi().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

class SmartContractAgent:
    def __init__(self, contract_address, contract_abi, network_url):
        # Connect to Ethereum network
        self.w3 = Web3(Web3.HTTPProvider(network_url))
        
        # Load contract
        self.contract_address = Web3.to_checksum_address(contract_address)
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=contract_abi)
        
        # Load environment variables
        load_dotenv()
        self.private_key = os.getenv('PRIVATE_KEY')
        self.account = Account.from_key(self.private_key)
        
        # Initialize state
        self.last_block = self.w3.eth.block_number
        self.gas_price_threshold = 50  # in gwei

# Example usage
def main():
    CONTRACT_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3"
    CONTRACT_ABI = """[
        {
        "inputs": [
            {
            "internalType": "address",
            "name": "newAIAgent",
            "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
        },
        {
        "inputs": [],
        "name": "DataMarketplace__NotAIAgent",
        "type": "error"
        },
        {
        "anonymous": false,
        "inputs": [
            {
            "indexed": true,
            "internalType": "uint32",
            "name": "dataIndex",
            "type": "uint32"
            },
            {
            "components": [
                {
                "internalType": "string",
                "name": "description",
                "type": "string"
                },
                {
                "internalType": "address",
                "name": "user",
                "type": "address"
                }
            ],
            "indexed": false,
            "internalType": "struct DataMarketplace.Data",
            "name": "data",
            "type": "tuple"
            },
            {
            "indexed": false,
            "internalType": "address",
            "name": "aiAgent",
            "type": "address"
            },
            {
            "indexed": false,
            "internalType": "bool",
            "name": "isValid",
            "type": "bool"
            }
        ],
        "name": "AIAgentResponded",
        "type": "event"
        },
        {
        "anonymous": false,
        "inputs": [
            {
            "indexed": true,
            "internalType": "uint32",
            "name": "dataIndex",
            "type": "uint32"
            },
            {
            "components": [
                {
                "internalType": "string",
                "name": "description",
                "type": "string"
                },
                {
                "internalType": "address",
                "name": "user",
                "type": "address"
                }
            ],
            "indexed": false,
            "internalType": "struct DataMarketplace.Data",
            "name": "data",
            "type": "tuple"
            }
        ],
        "name": "NewDataCreated",
        "type": "event"
        },
        {
        "inputs": [],
        "name": "aiAgent",
        "outputs": [
            {
            "internalType": "address",
            "name": "",
            "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
        },
        {
        "inputs": [
            {
            "internalType": "uint256",
            "name": "",
            "type": "uint256"
            }
        ],
        "name": "aiTrainingData",
        "outputs": [
            {
            "internalType": "string",
            "name": "description",
            "type": "string"
            },
            {
            "internalType": "address",
            "name": "user",
            "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
        },
        {
        "inputs": [
            {
            "internalType": "string",
            "name": "description",
            "type": "string"
            }
        ],
        "name": "createNewData",
        "outputs": [
            {
            "components": [
                {
                "internalType": "string",
                "name": "description",
                "type": "string"
                },
                {
                "internalType": "address",
                "name": "user",
                "type": "address"
                }
            ],
            "internalType": "struct DataMarketplace.Data",
            "name": "",
            "type": "tuple"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
        },
        {
        "inputs": [],
        "name": "latestDataNum",
        "outputs": [
            {
            "internalType": "uint32",
            "name": "",
            "type": "uint32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
        },
        {
        "inputs": [
            {
            "components": [
                {
                "internalType": "string",
                "name": "description",
                "type": "string"
                },
                {
                "internalType": "address",
                "name": "user",
                "type": "address"
                }
            ],
            "internalType": "struct DataMarketplace.Data",
            "name": "data",
            "type": "tuple"
            },
            {
            "internalType": "uint32",
            "name": "referenceDataIndex",
            "type": "uint32"
            },
            {
            "internalType": "bool",
            "name": "isValid",
            "type": "bool"
            }
        ],
        "name": "respondToNewData",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
        }
    ]"""

    NETWORK_URL = "http://127.0.0.1:8545"
    
    newContract = SmartContractAgent(CONTRACT_ADDRESS, CONTRACT_ABI, NETWORK_URL)

if __name__ == "__main__":
    main()