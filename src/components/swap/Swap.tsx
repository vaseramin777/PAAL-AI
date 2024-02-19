// Import necessary libraries and components
import React, { useEffect, useState } from "react";
import { Combobox } from "@headlessui/react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faChevronDown,
} from "@fortawesome/free-solid-svg-icons";
import Button from "../site/Button.tsx";
import {
  connectorsForWallets,
  RainbowKitProvider,
} from "@rainbow-me/rainbowkit";
import { configureChains, createConfig, WagmiConfig } from "wagmi";
import { mainnet } from "wagmi/chains";
import { publicProvider } from "wagmi/providers/public";
import { injectedWallet, metaMaskWallet, rainbowWallet } from "@rainbow-me/rainbowkit/wallets";
import { parseEther, parseUnits } from "viem";
import PaalTokLogo from "../../assets/site/paal-token.jpeg";

// Define the Swap component
export default function Swap() {
  // Initialize state variables
  const [availableTokens, setAvailableTokens] = useState<any[]>([]);
  const [selectedTokenSymbol, setSelectedTokenSymbol] = useState("ETH");
  const [equivalentPAALAmount, setEquivalentPAALAmount] = useState(0);
  const [paalTokenInfo, setPaalTokenInfo] = useState<any>({});
  const [wEthTokenInfo, setWethTokenInfo] = useState<any>({});

  // Fetch and set available tokens when the component mounts
  useEffect(() => {
    const whitelistedTokens = ["ETH", "USDT", "USDC"];
    const API_URL = "https://www.okx.com/api/v5/dex/aggregator";
    fetch(API_URL + "/all-tokens?chainId=1")
      .then((res) => res.json())
      .then((data) => {
        if (!data) return;
        const allowedTokens = data.data.filter((token: any) => {
          return whitelistedTokens.includes(token.tokenSymbol);
        });
        setAvailableTokens(allowedTokens);
        const paalTokenInfo = data.data.find(
          (token: any) => token.tokenSymbol === "PAAL"
        );
        setPaalTokenInfo(paalTokenInfo);
        const wEthTokenInfo = data.data.find(
          (token: any) => token.tokenSymbol === "WETH"
        );
        setWethTokenInfo(wEthTokenInfo);
      });
  }, []);

  // Set the selected token object based on the selected token symbol
  const selectedToken =
    selectedTokenSymbol === "ETH"
      ? {
          ...availableTokens.find(
            (token) => token?.tokenSymbol === selectedTokenSymbol
          ),
          tokenContractAddress: wEthTokenInfo?.tokenContractAddress,
        }
      : availableTokens.find(
          (token) => token?.tokenSymbol === selectedTokenSymbol
        );

  // Initialize state variable for token amount
  const [tokenAmount, setTokenAmount] = useState("1");

  // Return the JSX for the Swap component
  return (
    <WagmiConfig config={wagmiConfig}>
      <RainbowKitProvider chains={chains}>
        <section className="site-content container swap-container">
          <h3>Swap $PAAL</h3>

          {/* Swap methods container */}
          <div
            className="swap-methods-container"
            style={{ display: "flex", gap: "1rem" }}
          >
            {/* Token swap section */}
            <div>
              <div className="swap-card">
                <div className="heading">
                  <span className="label">From</span>
                  <img
                    src={selectedToken?.tokenLogoUrl}
                    alt=""
                    className="swap-coin-icon"
                  />
                  <span className="coin-name">
                    {selectedToken?.tokenName}
                  </span>
                </div>

                <div className="select-row" style={{ marginBottom: "3rem" }}>
                  <div>
                    <TokenSelect
                      availableTokens={availableTokens}
                      selectedToken={selectedTokenSymbol}
                      setSelectedToken={setSelectedTokenSymbol}
                      selectedTokenImage={
                        selectedToken?.tokenLogoUrl || PaalTokLogo
                      }
                    />
                  </div>

                  <div className="stats">
                    <input
                      type="number"
                      placeholder="1"
                      value={tokenAmount}
                      onChange={(e) => {
                        setTokenAmount(e.target.value);
                      }}
                      onBlur={(e) => {
                        const numAmount = parseFloat(e.target.value);
                        setTokenAmount(
                          numAmount > 0 ? numAmount.toString() : "1"
                        );
                      }}
                    />
                    {/*<span>$1,869.81</span>*/}
                  </div>
                </div>

                <div className="select-row">
                  <div className="token-search">
                    <img
                      src={paalTokenInfo?.tokenLogoUrl || PaalTokLogo}
                      alt=""
                      className="coin-icon"
                    />
                    <span className="input">PAAL</span>
                  </div>

                  <div className="stats">
                    <input
                      disabled
                      type="number"
                      value={equivalentPAALAmount.toFixed(2)}
                    />
                  </div>
                </div>
              </div>

              <div className="connect-button-container">
                <TokenSwapButton
                  selectedToken={selectedToken}
                  amount={tokenAmount}
                  setEquivalentAmount={setEquivalentPAALAmount}
                />

                <ConnectButton />
              </div>
