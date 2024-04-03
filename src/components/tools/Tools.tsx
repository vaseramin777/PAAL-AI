import { useState } from "react";
import Button from "../site/Button"; // Importing Button component

interface ContentItem {
  title: string;
  action: {
    label: string;
    link: string;
  };
  messages: {
    title: string;
    text: string;
  }[];
}

const Tools = () => {
  const [selectedIndex, setSelectedIndex] = useState(0);

  const content: ContentItem[] = [
    {
      title: "MyPaal",
      action: {
        label: "Set up MyPaal",
        link: "https://app.paal.ai/",
      },
      messages: [
        // ...
      ],
    },
    {
      title: "AutoPaal",
      action: {
        label: "Try Now",
        link: "https://t.me/mypaalbot",
      },
      messages: [
        // ...
      ],
    },
    {
      title: "AutoPaal X",
      action: {
        label: "Coming Soon",
        link: "/",
      },
      messages: [
        // ...
      ],
    },
  ];

  return (
    <section className="tools-container site-content-container">
      <h2 className="tools-heading">PAAL AI Tools</h2>

      <div className="split">
        <div className="selectors">
          {content.map((item, i) => (
            <div
              className={`selector ${i === selectedIndex ? "selected" : ""}`}
              onClick={() => setSelectedIndex(i)}
              key={item.title}
            >
              <span>{item.title}</span>
            </div>
          ))}
        </div>

        <div className="content">
          <ol className="list">
            {content[selectedIndex]?.messages?.map((message, i) => (
              <li key={i}>
                <span className="li-title">{message.title}</span> : {message.text}
              </li>
            ))}
          </ol>

          <div className="action">
            <Button
              label={content[selectedIndex].action.label}
              link={content[selectedIndex].action.link}
              mini={true}
            />
          </div>
        </div>
      </div>
    </section>
  );
};

export default Tools;
