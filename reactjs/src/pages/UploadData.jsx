import React, { useState } from 'react';
import { ethers } from 'ethers';

import DataMarketplaceContract from '../artifacts/contracts/DataMarketplace.sol/DataMarketplace.json';

const UploadData = () => {
  const [ethAddress, setETHAddress] = useState('');
  const [userSigner, setUserSigner] = useState(null);
  
  const connectWallet = async () => {
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    setETHAddress(accounts[0]);
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    setUserSigner(signer);
    const DataMarketplace = new ethers.Contract("0x5FbDB2315678afecb367f032d93F642f64180aa3", DataMarketplaceContract.abi, userSigner);
    console.log(DataMarketplace);
  }

  return (
    <div className="w-full max-w-lg mx-auto bg-white rounded-lg shadow-lg p-6 mt-10">
      <button
        onClick={connectWallet}
        className="w-full py-2 px-4 bg-blue-600 mb-4 cursor-pointer text-white rounded-md hover:bg-blue-700 transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:bg-blue-400 disabled:cursor-not-allowed flex items-center justify-center"
      >
        {ethAddress ? ethAddress.slice(0, 5) + "..." + ethAddress.slice(37, 42) : 'Connect Wallet'}
      </button>
    </div>
  );
};

export default UploadData;