import { FC } from "react";
import "./Header.scss";

import PAALAILogo from "../../assets/site/paal-ai-logo.png";
import MobileNavigation from "./MobileNavigation";
// import Button from "./Button";

const Header: FC = () => {
  const handleLogoClick = () => {
    // handle click event
  };

  const handleLogoKeyDown = (event: React.KeyboardEvent<HTMLDivElement>) => {
    if (event.key === "Enter" || event.key === "Space") {
      handleLogoClick();
    }
  };

  const handleMobileNavigationKeyDown = (event: React.KeyboardEvent<HTMLDivElement>) => {
    if (event.key === "Enter" || event.key === "Space") {
      // handle click event
    }
  };

  return (
    <header className="site-header site-content-container" title="Site Header">
      <div role="button" tabIndex={0} onClick={handleLogoClick} onKeyDown={handleLogoKeyDown} onFocus={() => {}} onBlur={() => {}}>
        <img src={PAALAILogo} alt="PAAL AI Logo" aria
