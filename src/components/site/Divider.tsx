import { FC, forwardRef } from "react";
import "./Divider.scss";

interface DividerProps {
  className?: string;
  orientation?: "horizontal" | "vertical";
}

const Divider: FC<DividerProps> = forwardRef((props, ref) => {
  const { className, orientation = "horizontal", ...rest } = props;

  return (
    <div
      ref={ref}
      className={`site-divider ${orientation} ${className}`}
      role={orientation === "horizontal" ? "separator" : undefined}
      aria-orientation={orientation}
      {...rest}
    />
  );
});

export default Divider;
