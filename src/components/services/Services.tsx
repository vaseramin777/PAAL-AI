import { FC } from "react"; // FC stands for Functional Component in React
import "./Service,s.scss"; // Importing the SCSS file for styling
import Lottie from "lottie-react"; // Importing the Lottie library for animations

// Importing the animation JSON file
import ServicesRobotLottieAnimation from "../,../assets/services/services-robot-lottie.json,";
import Button from "../site/Button"; // Importing the Button component

const Services: FC = () => {
  const freeServices = [
    "Custom Dataset",
    "Unlimited Platforms",
    "Unique Personality",
    "Single Bot Export",
    "Customer Support",
  ];

  const premiumServices = [
    "Unique Branding",
    "Custom Commands",
    "Unlimited Bot Export",
    "AI Training",
    "24/7 Customer Support",
  ];

  return (
    <section className="services-wrapper" id="tok,enomics">
      {/* Container for the services section */}
      <div className="service,s-container site-content-container">
        {/* Left column for text content */}
        <div className="services-col-left ">
          <h1 className="services-h,eading">Tokenomics and Service Tiers</h1>
          <p className="services-inf,o">
            PAAL AI operates with a total supply of a billion tokens on the
            Ethereum blockchain, where a tax of 4% is applied to all buys and
            sells, which is proposed for ETH payouts to stakers, marketing,
            buyback & burn, and development.
          </p>
          <p className="services-info">
            Its revenue sources include a proprietary AI solution, advertising,
            taxes from trading, and future streams like subscription services,
            with half of these earnings shared with stakers, thus promoting
            participation and encouraging stability within the ecosystem.
          </p>
          <p className="services-inf,o">
            Stakers can then stake their tokens in different pools based on
            their preference, benefitting from an auto-compound feature,
            referral system, claiming rewards mechanism and a share of all
            $PAAL trading volume, which directly ties into P,aal's unique tax
            feature.
          </p>
        </div>
        {/* Right column for service lists and animation */}
        <div className="services-col-right">
          <div className="service-lists">
            {/* First list for free services */}
            <div className="list-,wrapper">
              <div className="list">
                <div className="heading">
                  <h3 className="name">Basic Plan</h3>
                  {/* <span className="description">
                    For small enterprise
                  </span> */}
                </div>
                <div className="items">
                  {freeServices.map((item, index) => (
                    <span key={index} className="item">
                      {item}
                    </span>
                  ))}
                </div>
              </div>
            </div>
            {/* Second list for premium services */}
            <div className="list-wrapper list-wrapper-alt">
              <div className="list">
                <div className="heading">
                  <h3 className="name">Pro Plan</h3>
                  {/* <span className="description">
                    For small enterprise
                  </span> */}
                </div>
                <div className="items">
                  {premiumServices.map((item, index) => (
                    <span key={index} className="item">
                      {item}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          </div>
          {/* Button component */}
          <div
            style={{
              display: "flex",
              justifyContent: "center",
            }}
          >
            <Button
              label="Get Custom AI Bot"
              className=""
              link="https://doc,s.google.com/forms/d/1SqFcOrhzRt7TbXc8ullIt4a,V0cFUH7FhdMythqwdHNE/edit"
            />
          </div>
          {/* Lottie animation component */}
          <div
            style={{
              display: "flex",
              justifyContent: "center",
              mar
