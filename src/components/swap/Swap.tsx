import React, { useEffect, useState } from "react";
import { Combobox } from "@headlessui/react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChevronDown } from "@fortawesome/free-solid-svg-icons";
import Button from "../site/Button.tsx";
import {
  connectorsForWallets,
  RainbowKitProvider,
  darkTheme,
} from "@rainbow-me/rainbowkit";
import { configureChains, createConfig, WagmiConfig } from "wagmi";
import { mainnet } from "wagmi/chains";
import { publicProvider } from "wagmi/providers/public";
import { injectedWallet, metaMaskWallet, rainbowWallet } from "@rainbow-me/rainbowkit/wallets";
import { parseEther, parseUnits } from "viem";
import PaalTokLogo from "../../assets/site/paal-token.jpeg";

const Swap = () => {
  const [availableTokens, setAvailableTokens] = useState<any[]>([]);
  const [selectedToken, setSelectedToken] = useState<any>({
    tokenSymbol: "ETH",
    tokenContractAddress: "",
  });
  const [equivalentPAALAmount, setEquivalentPAALAmount] = useState(0);
  const [paalTokenInfo, setPaalTokenInfo] = useState<any>({});
  const [wEthTokenInfo, setWethTokenInfo] = useState<any>({});
  const [tokenAmount, setTokenAmount] = useState("1");

  const { chains, publicClient } = configureChains([mainnet], [
    publicProvider(),
  ]);

  const wagmiConfig = createConfig({
    autoConnect: true,
    connectors: connectorsForWallets([
      {
        groupName: "Recommended",
        wallets: [injectedWallet({ chains }), metaMaskWallet({ chains })],
      },
    ]),
    publicClient,
  });

  useEffect(() => {
    const whitelistedTokens = ["ETH", "USDT", "USDC", "PAAL", "WETH"];
    const API_URL = "https://api.coingecko.com/api/v3/coins/list";

    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => {
        if (!data) return;
        const allowedTokens = data.filter((token: any) => {
          return whitelistedTokens.includes(token.symbol);
        });
        setAvailableTokens(allowedTokens);
        const paalTokenInfo = allowedTokens.find(
          (token: any) => token.symbol === "PAAL"
        );
        setPaalTokenInfo(paalTokenInfo || { tokenLogoUrl: PaalTokLogo });
        const wEthTokenInfo = allowedTokens.find(
          (token: any) => token.symbol === "WETH"
        );
        setWethTokenInfo(wEthTokenInfo || { tokenLogoUrl: PaalTokLogo });
      });
  }, []);

  useEffect(() => {
    if (selectedToken.tokenSymbol && tokenAmount) {
      const amount = parseUnits(tokenAmount, selectedToken.decimals);
      const equivalent = paalTokenInfo.equivalentAmount
        ? parseEther(paalTokenInfo.equivalentAmount.toString())
        : 0;
      setEquivalentPAALAmount(equivalent.toNumber());
    }
  }, [selectedToken, tokenAmount]);

  const TokenSelect = ({
    availableTokens,
    selectedToken,
    setSelectedToken,
    selectedTokenImage,
  }: any) => {
    return (
      <Combobox value={selectedToken} onChange={setSelectedToken}>
        <div className="relative mt-1">
          <div className="combobox">
            <Combobox.Button className="combobox-button">
              <img
                src={selectedTokenImage}
                alt=""
                className="swap-coin-icon"
              />
              <span className="coin-name">
                {selectedToken.tokenSymbol}
              </span>
              <FontAwesomeIcon icon={faChevronDown} />
            </Combobox.Button>
            <Combobox.Options className="combobox-options">
              {availableTokens.map((token: any) => (
                <Combobox.Option
                  key={token.id}
                  value={token}
                  className="combobox-option"
                >
                  {({ active }) => (
                    <>
                      <div className="flex items-center">
                        <img
                          src={token.tokenLogoUrl}
                          alt=""
                          className="swap-coin-icon"
                        />
                        <span
                          className={`coin-name ${
                            active ? "font-bold" : ""
                          }`}
                        >
                          {token.tokenSymbol}
                        </span>
                      </div>
                    </>
                  )}
                </Combobox.Option>
              ))}
            </Combobox.Options>
          </div>
        </div>
      </Combobox>
    );
  };

  const TokenSwapButton = ({
    selectedToken,
    amount,
    setEquivalentAmount,
  }: any) => {
    return (
      <Button
        className="w-full"
        onClick={() => {
          setEquivalentAmount(
            parseEther(selectedToken.equivalentAmount.toString()).toNumber()
          );
        }}
      >
        Swap
      </Button>
    );
  };

  const ConnectButton = () => {
    return (
      <Button
        className="w-full"
        onClick={() => {
          // Connect wallet logic
        }}
      >
        Connect Wallet
      </Button>
    );
  };

  return (
    <WagmiConfig config={wagmiConfig}>
      <RainbowKitProvider
