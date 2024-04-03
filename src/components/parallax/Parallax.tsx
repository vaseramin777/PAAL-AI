import { FC, useEffect, useRef, useState } from "react";
import "./Parallax.scss";
import TRUNK from "vanta/src/vanta.trunk.js";
import p5 from "p5";
import { useInView } from "react-intersection-observer";
import Discover from "../discover/Discover";

const Parallax: FC = () => {
  const [vantaEffect, setVantaEffect] = useState(null);
  const vantaRef = useRef(null);

  useEffect(() => {
    if (!vantaEffect) {
      setVantaEffect(
        TRUNK({
          p5,
          el: vantaRef.current,
          mouseControls: true,
          touchControls: true,
          gyroControls: false,
          minHeight: 200.0,
          minWidth: 200.0,
          scale: 1.0,
          scaleMobile: 1.0,
          color: 0x882db1,
          backgroundColor: 0x0,
          spacing: 8.0,
          chaos: 4.0,
        })
      );
    }

    return () => {
      if (vantaEffect) vantaEffect.destroy();
    };
  }, [vantaEffect]);

  const parallaxTexts = [
    {
      label: "/paal Hola Paal, ¿cuéntame sobre el proyecto?",
      alternative: false,
      offset: 0,
    },
    {
      label: "/paal Hello Paal, 告诉我有关该项目的信息",
      alternative: true,
      offset: 70,
    },
    {
      label: "/paal Hallo Paal, erzähl mir etwas über das Projekt?",
      alternative: false,
      offset: 140,
    },
  ];

  return (
    <section className="parallax-container">
      <div className="vanta-background" ref={vantaRef}>
        <InitialParallaxItem
          label={"/paal Hello Paal, Tell Me About The Project?"}
          alternative={false}
          offset={-100}
        />
      </div>

      {parallaxTexts.map((textObj, index) => (
        <ParallaxItem key={index} {...textObj} />
      ))}

      <div
        style={{
          position: "sticky",
          background: "black",
        }}
      >
        <Discover />
      </div>
    </section>
  );
};

type ParallaxItemProps = {
  label: string;
  alternative: boolean;
  offset: number;
};

const ParallaxItem: FC<ParallaxItemProps> = ({ label, alternative, offset }) => {
  const { ref, inView } = useInView({
    threshold: 0.4,
  });

  const [shownText, setShownText] = useState("");

  useEffect(() => {
    const RATE = 50;

    if (inView) {
      const interval = setInterval(() => {
        setShownText((curr) => label.slice(0, curr.length + 1));
      }, RATE);

      return () => clearInterval(interval);
    } else {
      setShownText("");
    }
  }, [inView, label]);

  return (
    <div
      className={`parallax-item ${alternative ? "alternative" : ""}`}
      ref={ref}
      style={{
        top: offset,
      }}
    >
      <span className="parallax-text">{shownText}</span>
    </div>
  );
};

type InitialParallaxItemProps = {
  label: string;
  alternative: boolean;
  offset: number;
};

const InitialParallaxItem: FC<InitialParallaxItemProps> = ({
  label,
  alternative,
  offset,
}) => {
  const { ref, inView } = useInView({
    threshold: 0.4,
  });

  const [shownText, setShownText] = useState("");

  useEffect(() => {
    const RATE = 50;

    if (inView) {
      const interval = setInterval(() => {
        setShownText((curr) => label.slice(0, curr.length + 1));
      }, RATE);

      return () => clearInterval(interval);
    } else {
      setShownText("");
    }
  }, [inView, label]);

  return (
    <div
      className={`initial-parallax-item ${alternative ? "alternative" : ""}`}
      ref={ref}
    >
      <span className="parallax-text">{shownText}</span>
    </div>
  );
};

export default Parallax;
