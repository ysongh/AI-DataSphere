// This setup uses Hardhat Ignition to manage smart contract deployments.
// Learn more about it at https://hardhat.org/ignition

const { buildModule } = require("@nomicfoundation/hardhat-ignition/modules");


module.exports = buildModule("DataMarketplaceModule", (m) => {
  const dataMarketplace = m.contract("DataMarketplace", ["0xF91Ca5BB6F157731DF516b1968A0e9046cc7Ed48"]);

  return { dataMarketplace };
});
