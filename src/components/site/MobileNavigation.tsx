import { FC, useState } from "react";
import "./MobileNavigation.scss";
import { FontAwesomeIcon, faBars } from "@fortawesome/react-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";

library.add(faBars);

const MobileNavigation: FC = () => {
  const links = [
    { label: "Home", url: "#home" },
    { label: "Discover", url: "#discover" },
    { label: "Stake", url: "#stake" },
    { label: "Features", url: "#features" },
    { label: "Video Tutorial", url: "#benefits" },
    { label: "Tokenomics", url: "#tokenomics" },
    { label: "Contact", url: "#whitelist" },
  ];

  const docsLinks = [
    { label: "Whitepaper", link: "/whitepaper.pdf" },
    { label: "GitBook", link: "https://docs.paalai.io/" },
    { label: "Medium", link: "https://medium.com/@admin_42570" },
  ];

  const [isNavigationOpen, setIsNavigationOpen] = useState(false);
  const [isDocsOpen, setIsDocsOpen] = useState(false);

  const toggleNavigation = () => {
    setIsNavigationOpen((prevState) => !prevState);
  };

  const toggleDocs = () => {
    setIsDocsOpen((prevState) => !prevState);
  };

  return (
    <>
      <button className="mobile-navigation-toggle" onClick={toggleNavigation}>
        <div className="mobile-navigation-toggle-icon-wrapper">
          <FontAwesomeIcon
            className={`mobile-navigation-toggle-icon ${isNavigationOpen ? "open" : ""}`}
            icon={faBars}
          />
          <span>Menu</span>
        </div>
      </button>

      <nav className={`mobile-navigation ${isNavigationOpen ? "open" : ""}`}>
        <ul className="mobile-navigation-list">
          {links.map(({ label, url }, index) => (
            <li className="mobile-navigation-list-item" key={index}>
              <a
                className="mobile-navigation-link"
                href={url}
                onClick={toggleNavigation}
              >
                {label}
              </a>
            </li>
          ))}
        </ul>

        <div className="more-items">
          <button className="more-items-toggle" onClick={toggleDocs}>
            Docs {!isDocsOpen ? "+" : "-"}
          </button>

          <ul className={`more-items-list ${isDocsOpen ? "shown" : ""}`}>
            {docsLinks.map(({ label, link }, index) => (
              <li key={index} className="more-item">
                <a
                  href={link}
                  onClick={(e) => {
                    e.stopPropagation();
                    toggleDocs();
                  }}
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
