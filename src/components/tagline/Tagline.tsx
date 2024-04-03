import { FC } from "react";
import styles from "./Tagline.module.scss"; // import styles as object

const Tagline: FC = () => {
  return (
    <section className={styles.taglineContainer}> {/* use imported styles */}
      <p className={styles.taglineText}>
        PAAL is a powerful AI ecosystem, predicated on principles of continuous learning and adaptation.
      </p>
    </section>
  );
};

export default Tagline;
