import { FC } from "react";
import "./Explore.scss";
import Button from "../site/Button";

const Explore: FC = () => {
  const featureCards = [
    {
      label: "Advanced AI and machine learning",
      url: "#advanced-ai",
    },
    {
      label: "Multi-platform integration",
      url: "#multi-platform",
    },
    {
      label: "Custom dataset training",
      url: "#custom-training",
    },
    {
      label: "Adaptable and Evolving",
      url: "#adaptable",
    },
  ];

  const rewardItems = [
    "1% of all $PAAL trading volume.",
    "AI tools subscription.",
    "Service revenue sharing.",
    "15% referral rewards.",
    "Partner projects Airdrops.",
  ];

  return (
    <section
      className="explore-container site-content-container"
      id="stake"
    >
      <p className="explore-info">
        PAAL is a robust AI ecosystem leveraging advanced AI and ML technologies.
        It enables users to create personalized AI, deploy it across multiple
        platforms including Telegram and Discord, and offers comprehensive AI
        solutions for businesses and projects
      </p>

      <div className="explore-cards">
        {featureCards.map((card, index) => (
          <ExploreCard key={index} {...card} />
        ))}
      </div>

      <h2 className="explore-heading">
        Revenue Sharing & Rewards for Stakers
      </h2>

      <ul className="explore-list">
        {rewardItems.map((text, index) => (
          <li key={index}>{text}</li>
        ))}
      </ul>

      <div className="center-items explore-actions">
        <Button
          label="Stake Now"
          mini
          link="https://rewards.paalai.io/"
        />
      </div>
    </section>
  );
};

type ExploreCardProps = {
  label: string;
  url: string;
};

const ExploreCard: FC<ExploreCardProps> = ({ label, url }) => {
  return (
    <a href={url} className="explore-card">
      <span className="explore-card-label">{label}</span>
    </a>
  );
};

export default Explore;
