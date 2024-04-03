import { FC } from "react";
import "./Socials.scss";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
    faDiscord,
    faFacebook,
    faInstagram,
    faLinkedin,
    faTelegram,
    faTwitter,
} from "@fortawesome/free-brands-svg-icons";
import DexToolsIcon from "../../assets/icons/dextools.svg";
import GeckoTerminalIcon from "../../assets/icons/geckoterminal.svg";
import BitMartIcon from "../../assets/icons/bitmart.png";
import GateIcon from "../../assets/icons/gate.png";

type SocialsProps = {
    large?: boolean;
    small?: boolean;
};

const Socials: FC<SocialsProps> = ({ large = false, small = false }) => {
    return (
        <div
            className={`
                socials
                ${large ? "large-icons" : ""}
                ${small ? "small-icons" : ""}
            `}
        >
            <a
                className="social-link"
                href={"https://twitter.com/PaalMind"}
                target="_blank"
                rel="noopener noreferrer"
                title="Twitter"
            >
                <FontAwesomeIcon
                    icon={faTwitter}
                    aria-label="Twitter"
                />
            </a>

            <a
                className="social-link"
                href={"https://t.me/paal_ai"}
                target="_blank"
                rel="noopener noreferrer"
                title="Telegram"
            >
                <FontAwesomeIcon
                    icon={faTelegram}
                    aria-label="Telegram"
                />
            </a>

            <a
                className="social-link"
                href={"https://discord.gg/paalai"}
                target="_blank"
                rel="noopener noreferrer"
                title="Discord"
            >
                <FontAwesomeIcon
                    icon={faDiscord}
                    aria-label="Discord"
                />
            </a>

            <a
                className="social-link"
                href={
                    "https://www.dextools.io/app/en/ether/pair-explorer/0x2a6c340bcbb0a79d3deecd3bc5cbc2605ea9259f"
                }
                target="_blank"
                rel="noopener noreferrer"
                title="DexTools"
            >
                <img src={DexToolsIcon} alt="DexTools" />
            </a>

            <a
                className="social-link"
                href={
                    "https://www.geckoterminal.com/eth/pools/0x2a6c340bcbb0a79d3deecd3bc5cbc2605ea9259f"
                }
                target="_blank"
                rel="noopener noreferrer"
                title="GeckoTerminal"
            >
                <img
                    src={GeckoTerminalIcon}
                    alt="GeckoTerminal"
                    style={{ filter: "grayscale(100%)" }}
                />
            </a>
            <a
                className="social-link"
                href={"https://www.bitmart.com/trade/en-US?symbol=PAAL_USDT"}
                target="_blank"
                rel="noopener noreferrer"
                title="BitMart"
            >
                <img
                    src={BitMartIcon}
                    alt="BitMart"
                    style={{ filter: "grayscale(100%)" }}
                />
            </a>
            <a
                className="social-link"
                href={"https://www.gate.io/trade/PAAL_USDT"}
                target="_blank"
                rel="noopener noreferrer"
                title="Gate"
            >
                <img
                    src={GateIcon}
                    alt="Gate"
                    style={{ filter: "grayscale(100%)" }}
                />
            </a>
            <a
                className="social-link"
                href={"https://www.facebook.com/"}
                target="_blank"
                rel="noopener noreferrer"
                title="Facebook"
            >
                <FontAwesomeIcon
                    icon={faFacebook}
                    aria-label="Facebook"
                />
            </a>
            <a
                className="social-link"
                href={"https://www.instagram.com/"}
                target="_blank"
                rel="noopener noreferrer"
                title="Instagram"
            >
                <FontAwesomeIcon
                    icon={faInstagram}
                    aria-label="Instagram"
                />
            </a>
            <a
                className="social-link"
                href={"https://www.linkedin.com/"}
                target="_
