import { FC } from "react";
import "./Services.scss";
import Lottie from "lottie-react";
import ServicesRobotLottieAnimation from "../assets/services/services-robot-lottie.json";
import Button from "../site/Button";

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
    <section className="services-wrapper" id="tokenomics">
      <div className="service-container site-content-container">
        <div className="services-col-left">
          <h1 className="services-heading">Tokenomics and Service Tiers</h1>
          <p className="services-info">
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
          <p className="services-info">
            Stakers can then stake their tokens in different pools based on
            their preference, benefitting from an auto-compound feature,
            referral system, claiming rewards mechanism and a share of all
            $PAAL trading volume, which directly ties into P,aal's unique tax
            feature.
          </p>
        </div>
        <div className="services-col-right">
          <div className="service-lists">
            <div className="list-wrapper">
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
          <div className="button-container">
            <Button
              label="Get Custom AI Bot"
              className=""
              link="https://docs.google.com/forms/d/1SqFcOrhzRt7TbXc8ullIt4aV0cFUH7FhdMythqwdHNE/edit"
            />
          </div>
          <div className="lottie-animation-container">
            <Lottie animationData={ServicesRobotLottieAnimation} />
          </div>
        </div>
      </div>
    </section>
  );
};

export default Services;
