import { FC } from "react";
import "./Sponsor.scss";

import GoogleCloudLogo from "../../assets/icons/google-cloud-logo.png";
import CoinGecko from "../../assets/icons/coingecko.webp";

type SponsorProps = {
    mobileCenter?: boolean;
};

const Sponsor: FC<SponsorProps> = ({ mobileCenter }) => {
    return (
        <div className={`sponsor ${mobileCenter ? "mobile-sponsor" : ""}`}>
            <span className="sponsor-title" aria-label="Supported by">
                Supported by
            </span>
            <img
                className="sponsor-icon"
                src={GoogleCloudLogo}
                alt="Google Cloud Platform"
                height={50}
                width={150}
                role="img"
                loading="lazy"
            />

            <a
                className="sponsor-icon"
                href="https://www.coingecko.com"
                rel="noopener noreferrer"
                title="Coin Gecko"
            >
                <img
                    className="sponsor-icon"
                    src={CoinGecko}
                    alt="Coin Gecko"
                    key={CoinGecko}
                    height={50}
                   
