import { FC } from "react";
import "./Services.scss";
import Lottie from "lottie-react";

import ServicesRobotLottieAnimation from "../../assets/services/services-robot-lottie.json";

const Services: FC = () => {
    const freeServices = [
        "AI bot",
        "One user",
        "Custom dataset",
        "Multi-platform integration",
    ];

    const premiumServices = [...freeServices, "Unlimited data storage"];

    return (
        <section className="services-container site-content-container">
            <div className="services-col-left">
                <h1 className="services-heading">
                    Tokenomics and Service Tiers
                </h1>

                <p className="services-info">
                    PAAL AI, a token on Ethereum, incentivizes holders with
                    profit sharing and token buybacks to drive token demand and
                    price.
                </p>

                <p className="services-info">
                    Users can earn tokens through interactions with our AI
                    service, making referrals, and contributing to the
                    community.
                </p>

                <p className="services-info">
                    Finally, tokens enable governance voting and can be staked
                    for interest, unlocking premium features. We also accept
                    Ethereum for service purchases, offering enticing discounts.
                </p>

                <Lottie animationData={ServicesRobotLottieAnimation} loop />
            </div>

            <div className="services-col-right">
                <div className="service-lists">
                    <div className="list">
                        <div className="heading">
                            <h3 className="name">Free model</h3>
                            <span className="description">
                                For small enterprise
                            </span>
                        </div>
                        <div className="items">
                            {freeServices.map((item) => (
                                <span className="item">{item}</span>
                            ))}
                        </div>
                    </div>

                    <div className="list">
                        <div className="heading">
                            <h3 className="name">Premium</h3>
                            <span className="description">
                                For small enterprise
                            </span>
                        </div>
                        <div className="items">
                            {premiumServices.map((item) => (
                                <span className="item">{item}</span>
                            ))}
                        </div>
                    </div>
                </div>

                <div className="service-titles">
                    <span className="title">Free</span>
                    <span className="title">Custom Price</span>
                </div>
            </div>
        </section>
    );
};

export default Services;
