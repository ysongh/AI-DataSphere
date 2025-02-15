import React, { useState } from 'react';
import { ethers } from 'ethers';

import DataMarketplaceContract from '../artifacts/contracts/DataMarketplace.sol/DataMarketplace.json';

const UploadData = () => {
  const [isConnected, setIsConnected] = useState(false);
  const [ethAddress, setETHAddress] = useState('');
  const [userSigner, setUserSigner] = useState(null);
  const [description, setDescription] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const connectWallet = async () => {
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    setETHAddress(accounts[0]);
    const provider = new ethers.BrowserProvider(window.ethereum);
    const signer = await provider.getSigner();
    setUserSigner(signer);
    setIsConnected(true);
  }

  const addData = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      if (!isConnected) {
        throw new Error('Please connect your wallet first');
      }

      if (!description.trim()) {
        throw new Error('Please enter description');
      }

      const DataMarketplace = new ethers.Contract("0x10502f20179230c67b17531355d7e439A27Fc924", DataMarketplaceContract.abi, userSigner);
      const transaction = await DataMarketplace.createNewData(description);
      const tx = await transaction.wait();
      console.log(tx);
      setLoading(false);
    } catch (error) {
      console.error(error.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md mx-auto bg-white rounded-lg shadow-md overflow-hidden">
        <div className="px-6 py-8">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">
            Submit Data to Marketplace
          </h2>

          <div className="mb-6">
            {!isConnected ? (
              <button
                onClick={connectWallet}
                disabled={loading}
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-md transition duration-150 ease-in-out disabled:opacity-50"
              >
                {loading ? 'Connecting...' : 'Connect Wallet'}
              </button>
            ) : (
              <div className="flex items-center justify-between bg-gray-50 px-4 py-2 rounded-md">
                <span className="text-sm text-gray-600">Connected:</span>
                <span className="text-sm font-medium text-gray-900 truncate ml-2">
                  {`${ethAddress.slice(0, 6)}...${ethAddress.slice(-4)}`}
                </span>
              </div>
            )}
          </div>

          <form onSubmit={addData} className="space-y-6">
            <div>
              <label 
                htmlFor="description" 
                className="block text-sm font-medium text-gray-700 mb-2"
              >
                Description
              </label>
              <textarea
                id="description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                rows={4}
                className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="Enter your data description..."
                disabled={!isConnected || loading}
              />
            </div>

            {error && (
              <div className="text-red-600 text-sm">
                {error}
              </div>
            )}

            <button
              type="submit"
              disabled={!isConnected || loading}
              className="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-2 px-4 rounded-md transition duration-150 ease-in-out disabled:opacity-50"
            >
              {loading ? 'Submitting...' : 'Submit Data'}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default UploadData;