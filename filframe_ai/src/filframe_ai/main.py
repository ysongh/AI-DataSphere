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
    
    def create_new_data(self):
        try:
            current_gas_price = self.w3.eth.gas_price
            if current_gas_price > self.gas_price_threshold * 10**9:
                print("Gas price too high, skipping transaction")
                return
            
            nonce = self.w3.eth.get_transaction_count(self.account.address)
            
            transaction = self.contract.functions.createNewData("Test").build_transaction({
                'from': self.account.address,
                'gas': 200000,
                'gasPrice': current_gas_price,
                'nonce': nonce,
            })
            
            tx_hash = self.w3.eth.send_transaction(transaction)
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            print(f"Transaction successful! Hash: {tx_hash.hex()}")
            
        except Exception as e:
            print(f"Error executing transaction: {e}")
    
    def respond_to_new_data(self):
        try:
            new_data = {
                'description': "Test",
                'user': Web3.to_checksum_address('0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC'),
            }
            current_gas_price = self.w3.eth.gas_price
            if current_gas_price > self.gas_price_threshold * 10**9:
                print("Gas price too high, skipping transaction")
                return
            
            nonce = self.w3.eth.get_transaction_count(self.account.address)
            
            transaction = self.contract.functions.respondToNewData(new_data, 2, True).build_transaction({
                'from': self.account.address,
                'gas': 200000,
                'gasPrice': current_gas_price,
                'nonce': nonce,
            })
            
            tx_hash = self.w3.eth.send_transaction(transaction)
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            print(f"Transaction successful! Hash: {tx_hash.hex()}")
            
        except Exception as e:
            print(f"Error executing transaction: {e}")

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
    newContract.respond_to_new_data()

if __name__ == "__main__":
    main()