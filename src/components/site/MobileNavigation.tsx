import { FC, useState } from "react";
import "./MobileNavigation.scss";
import { FontAwesomeIcon, faBars } from "@fortawesome/react-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";

// Add the faBars icon to the library
library.add(faBars);

const MobileNavigation: FC = () => {
  // Define the navigation links
  const links = [
    { label: "Home", url: "#home" },
    { label: "Discover", url: "#discover" },
    { label: "Stake", url: "#stake" },
    { label: "Features", url: "#features" },
    { label: "Video Tutorial", url: "#benefits" },
    { label: "Tokenomics", url: "#tokenomics" },
    { label: "Contact", url: "#whitelist" },
  ];

  // Define the state for controlling the navigation visibility
  const [isNavigationOn, setIsNavigationOn] = useState(false);

  // Function to toggle the mobile navigation
  const toggleMobileNavigation = () => {
    setIsNavigationOn((p) => !p);
  };

  // Function to turn off the mobile navigation
  const turnOffMobileNavigation = () => {
    setIsNavigationOn(false);
  };

  // Define the state for controlling the docs visibility
  const [isDocsShown, setIsDocsShown] = useState(false);

  // Function to toggle the docs visibility
  const toggleDocs = (e: React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
    e.stopPropagation();

    setIsDocsShown((p) => !p);
  };

  // Function to turn off the docs visibility
  const turnOffDocs = (e: React.MouseEvent<HTMLAnchorElement, MouseEvent>) => {
    e.stopPropagation();

    setIsDocsShown(false);
  };

  // Define the docs links
  const docsLinks = [
    { label: "Whitepaper", link: "/whitepaper.pdf" },
    { label: "GitBook", link: "https://docs.paalai.io/" },
    { label: "Medium", link: "https://medium.com/@admin_42570" },
  ];

  return (
    <>
      {/* Button to toggle the mobile navigation */}
      <button
        className="mobile-navigation-toggle"
        onClick={toggleMobileNavigation}
      >
        <div className="mobile-navigation-toggle-icon-wrapper">
          {/* FontAwesome icon for the hamburger menu */}
          <FontAwesomeIcon
            className={`mobile-navigation-toggle-icon ${
              isNavigationOn ? "open" : ""
            }`}
            icon={faBars}
          />

          {/* Label for the menu button */}
          <span>Menu</span>
        </div>
      </button>

      {/* The mobile navigation itself */}
      <nav
        className={`mobile-navigation ${isNavigationOn ? "open" : ""}`}
        onClick={turnOffMobileNavigation}
      >
        {/* The list of navigation links */}
        <ul className="mobile-navigation-list">
          {links.map(({ label, url }, index) => (
            <li className="mobile-navigation-list-item" key={index}>
              {/* The actual navigation link */}
              <a
                className="mobile-navigation-link"
                href={url}
                onClick={turnOffMobileNavigation}
              >
                {label}
              </a>
            </li>
          ))}
        </ul>

        {/* The "More Items" section */}
        <div className="more-items">
          {/* Button to toggle the docs visibility */}
          <button className="more-items-toggle" onClick={toggleDocs}>
            Docs {!isDocsShown ? "+" : "-"}
          </button>

          {/* The list of docs links */}
          <ul
            className={`more-items-list ${isDocsShown ? "shown" : ""}`}
          >
            {docsLinks.map(({ label, link }, index) => (
              <li key={index} className="more-item">
                {/* The actual docs link */}
                <a
                  href={link}
                  onClick={turnOffDocs}
                  className="more-item-link"
                >
                  {label}
                </a>
              </li>
            ))}
          </ul>
        </div>
      </nav>
    </>
  );
};

export default MobileNavigation;
