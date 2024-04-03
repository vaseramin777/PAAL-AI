import "./Partners.scss";

// Importing image components for the partners
import GCloudImage from "../../assets/partners/gcloud.png";
import OKXImage from "../../assets/partners/okx.png";
import AminoIcon from "../../assets/icons/Amino.png";
import CoinGeckoIcon from "../../assets/icons/coingecko.webp";
import GeckoTerminalIcon from "../../assets/icons/GeckoTerminal.webp";
// import NvidiaIcon from "../../assets/icons/nvidia-logo.png";

export default function Partners() {
   return (
        <section className="site-content-container partners-container">
            {/* Heading for the partners section */}
            <h2>Partners</h2>
            <div className="partners">
                <div className="images">
                    {/* Individual partner images */}
                    <figure className="aminoIcon">
                        <img className="image" src={AminoIcon} alt="Amino logo" />
                        <figcaption className="figure-caption">Amino</figcaption>
                    </figure>
                    <figure>
                        <img className="image" src={GCloudImage} alt="Google Cloud logo" />
                        <figcaption className="figure-caption">Google Cloud</figcaption>
                    </figure>
                    <figure>
                        <img className="image" src={OKXImage} alt="OKX logo" />
                        <figcaption className="figure-caption">OKX</figcaption>
                    </figure>
                    <figure className="coincecko">
                        <img className="image" src={CoinGeckoIcon} alt="CoinGecko logo" />
                        <figcaption className="figure-caption">CoinGecko</figcaption>
                    </figure>
                </div>
                <div className="images2">
                    {/* <img src={CoinGeckoIcon} alt="" /> */}
                    {/* <img src={NvidiaIcon} alt="" /> */}
                    <figure>
                        <img className="image" src={GeckoTerminalIcon} alt="GeckoTerminal logo" />
                        <figcaption className="figure-caption">GeckoTerminal</figcaption>
                    </figure>
                    <div className="images3 chainlink-badges">
                        {/* Chainlink badges */}
                        <a
                            href="https://chain.link/badge"
                            target="_blank"
                            aria-label="market data secured with chainlink"
                        >
                            <img
                                className="image"
                                src="https://uploads-ssl.webflow.com/5f6b7190899f41fb70882d08/632c50d9db40967f015be6d1_secured-with-chainlink-badge-market-data.svg"
                                alt="market data secured with chainlink"

