// This setup uses Hardhat Ignition to manage smart contract deployments.
// Learn more about it at https://hardhat.org/ignition

const { buildModule } = require("@nomicfoundation/hardhat-ignition/modules");


module.exports = buildModule("DataMarketplaceModule", (m) => {
  const dataMarketplace = m.contract("DataMarketplace", ["0x70997970C51812dc3A010C7d01b50e0d17dc79C8"]);

  return { dataMarketplace };
});
