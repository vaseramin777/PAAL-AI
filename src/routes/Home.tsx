import { FC, PropsWithChildren } from "react";
import Hero from "../components/home/Hero";
import Parallax from "../components/parallax/Parallax";
import Features from "../components/features/Features";
import Benefits from "../components/benefits/Benefits";
import Divider from "../components/site/Divider";
import Explore from "../components/explore/Explore";
import Tagline from "../components/tagline/Tagline";
import Services from "../components/services/Services";
import Whitelist from "../components/whitelist/Whitelist";
import Footer from "../components/site/Footer";
import Tools from "../components/tools/Tools";
import Partners from "../components/partners/Partners";

// Lazy-load the components that are not always needed
const LazySwap = React.lazy(() => import("../components/swap/Swap"));

const Home: FC<PropsWithChildren> = () => {
  return (
    <>
      {/* <MobileNavigation /> */}

      <Hero
        title="Welcome to our platform"
        description="Discover a new way to interact with our services."
        img1Alt="Hero image 1"
        img2Alt="Hero image 2"
      />

      <Divider />
      <Parallax />
      <Divider />

      {/* NOT ACCESSED FROM HERE */}
      {/* <Discover /> */}

      <Explore />
      <Divider />

      <Tools />

      <Divider />
      <Tagline />
      <Divider />

      <Features />

      <Benefits />

      {/* <Empowered /> */}

      <Divider />
      <Suspense fallback={<div>Loading Swap component...</div>}>
        <LazySwap />
      </Suspense>
      <Divider />

      <Services />

      <Partners />

      <Whitelist
