import { FC } from "react";
import "./ColorDrops.scss";

interface ColorDropProps {
  index: number;
}

const ColorDrop: FC<ColorDropProps> = ({ index }) => {
  return <div key={index} className="color-drop" />;
};

const ColorDrops: FC = () => {
  const colorDropsCount = 144;

  return (
    <div className="color-drops-container">
      {Array.from({ length: colorDropsCount }, (_, index) => (
        <ColorDrop key={index} index={index} />
      ))}
    </div>
  );
};

export default ColorDrops;
