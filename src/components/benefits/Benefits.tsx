import React from "react";
import "./Benefits.scss";
import Stats from "../stats/Stats";

const BenefitsShowcaseItem = (props: { background: string }) => {
  return <img src={props.background} alt="" className="benefits-showcase-item" />;
};

const Benefits = () => {
  const benefitsShowcaseItemsRowOne = [
    "benefits-showcase-1.png",
    "benefits-showcase-2.png",
  ];

  const benefitsShowcaseItemsRowTwo = [
    "benefits-showcase-3.png",
    "benefits-showcase-4.png",
  ];

  return (
    <section className="benefits-container" id="benefits">
      <h1 className="benefits-heading site-content-container benefits-mobile-hidden">
        Setup my bot
      </h1>

      <div className="benefits-gallery site-content-container benefits-mobile-hidden">
        <div className="benefits-showcase-row">
          {benefitsShowcaseItemsRowOne.map((item, index) => (
            <BenefitsShowcaseItem
              key={index}
              background={item}
            />
          ))}
        </div>

        <img
          src="benefits-robot.png"
          alt="Benefits Showcase"
          className="benefits-showcase-image"
        />

        <div className="benefits-showcase-row">
          {benefitsShowcaseItemsRowTwo.map((item, index) => (
            <BenefitsShowcaseItem
              key={index}
              background={item}
            />
          ))}
        </div>
      </div>

      <iframe
        className="benefits-video site-content-container"
        width="560"
        height="315"
        src="https://www.youtube-nocookie.com/embed/7H_DmlVMqdU"
        title="YouTube video player"
        frameBorder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowFullScreen
      ></iframe>

      <p className="benefits-info site-content-container">
        Leverage the strength of machine learning with PAAL, using algorithms
        that construct models from training data, facilitating informed
        predictions or decisions
      </p>

      <Stats />
    </section>
  );
};

export default Benefits;
