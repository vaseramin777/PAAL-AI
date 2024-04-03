import React from "react";
import ReactDOM from "react-dom/client";
import Home from "./routes/Home";
import "./styles/main.scss";

try {
  const root = ReactDOM.createRoot(document.getElementById("root") as HTMLElement);
  root.render(
    <React.StrictMode>
      <title>My App</title>
      <Home />
    </React.StrictMode>
  );
} catch (err) {
  console.error("Error rendering the app", err);
}
