import { FC } from "react";
import "./Discover.scss";

// TODO: get proper transparent image
import DiscoverRobotImage from "../../assets/discover/discover-robot.png";
import Sponsor from "../site/Sponsor";
import Divider from "../site/Divider";

const Discover: FC = () => {
    return (
        <>
            <Divider title="Divider" aria-hidden="true" />
            <section className="discover-container" id="discover" role="region" aria-label="Discover Section">
                <span className="discover-sub-heading">Discover</span>
                <h1 className="discover-heading">
                    The power of AI & machine learning
                </h1>

                <div className="discover-graphic-container">
                    <img
                        src={DiscoverRobotImage}
                        alt="Discover Robot"
                        title="Transparent robot image for Discover section"
                        className="discover-graphic"
                        height="300"
                        width="300"
                        decoding="async"
                    />

                    <div className="sponsor-container">
                        <Sponsor alt="Sponsor logo" />
                    </div>
                </div>
            </section>
        </>
    );
};

export default Discover;
