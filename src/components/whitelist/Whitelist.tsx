import { FC } from "react";
import "./Whitelist.scss";
import Button from "../site/Button";

const Whitelist: FC = () => {
  return (
    <section className="whitelist-section" id="whitelist">
      <div className="content site-content-container">
        <h3>
          <span>Sign up for </span>
          <span>&nbsp;Paal AI Mobile app waitlist</span>{" "}
        </h3>
        <p>
          Be the first to know when Paal AI Mobile app is launched. Sign up for
          our waitlist now!
        </p>
        <Button
          data-testid="join-waitlist-button"
          link="https://forms.gle/uSvA2eFk9M5nk4ZP9"
          label=" Join Waitlist"
          aria-label="Join Paal AI Mobile app waitlist"
          target="_blank"
          rel="noopener noreferrer"
        />
      </div>
    </section>
  );
};

export default Whitelist;
