// Import necessary modules and components
import { FC, useEffect, useState } from "react";
import "./Empowered.scss";
import { useInView } from "react-intersection-observer";
import EmpoweredImage from "../../assets/empowered/empowered.png";
import EmpoweredShowcaseImage from "../../assets/empowered/empowered-showcase.png";
// import BubbleFloat from "../transitions/BubbleFloat";
import Services from "../services/Services";

// Define the Parallax component
const Parallax: FC = () => {
  // Define the parallaxTexts array
  const parallaxTexts = [
    "PAAL is empowered by",
    "cutting-edge machine",
    "learning algorithms",
  ];

  return (
    <section className="empowered-parallax-container">
      {/* <div className="vanta-background" ref={vantaRef} /> */}
      <div
        className="empowered-background"
        style={{
          backgroundImage: `
                        linear-gradient(
                            rgba(0, 0, 0, 0.1),
                            rgba(0, 0, 0, 0.6)
                        ),
                   url(${EmpoweredImage})
                 `,
        }}
      />

      <img
        src={EmpoweredShowcaseImage}
        alt="Empowered Showcase"
        className="empowered-showcase"
      />

      {parallaxTexts.map((text, index) => (
        <ParallaxItem
          key={index}
          label={text}
          mini={index === 0}
          offset={index * 75 + 160}
        />
      ))}

      {/* SPACER */}
      <div style={{ height: "30vh" }} />

      {/* <div className="parallax-item" style={{ background: "black" }}>
        <Services />
      </div> */}

      <div
        style={{
          position: "sticky",
          background: "black",
        }}
      >
        {/* <BubbleFloat /> */}
        <Services />
      </div>
    </section>
  );
};

// Export the Parallax component
export default Parallax;

// Define the ParallaxItem component props
type ParallaxItemProps = {
  label: string;
  mini: boolean;
  offset: number;
};

// Define the ParallaxItem component
const ParallaxItem: FC<ParallaxItemProps> = ({ label, mini, offset }) => {
  // Declare the ref and inView state variables
  const { ref, inView } = useInView({
    threshold: 0,
  });

  // Declare the shownText state variable
  const [shownText, setShownText] = useState("");

  // Define the useEffect hook to update the shownText state variable
  useEffect(() => {
    const RATE = 50;

    if (inView) {
      const interval = setInterval(() => {
        setShownText((curr) => label.slice(0, curr.length + 1));
      }, RATE);

      // Clean up the interval on component unmount
      return () => clearInterval(interval);
    } else {
      setShownText("");
    }
  }, [inView, label]);

  return (
    <div
      className="empowered-item"
      ref={ref}
      style={{ top: offset }}
    >
      <span
        className={`${mini ? "empowered-text-mini" : ""} empowered-text`}
      >
        {shownText}
      </span>
    </div>
  );
};
