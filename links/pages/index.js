import Head from "next/head";
import { PrimaryButton, SecondaryButton } from "../components/Buttons";
import links from "../lib/links";

export default function Home() {
  return (
    <div id="home-root">
      <Head>
        <title>{"Vaidyuti Services Links"}</title>
      </Head>
      <section className="bg-black py-24 px-8">
        <div className="container mx-auto max-w-screen-xl">
          <h2 className="inline-block w-auto text-gray-100 lg:mb-3">
            <small className="text-primary tracking-widest flex items-center text-base font-bold uppercase after:bg-brand mb-3 ml-1">
              Active Services
            </small>
            Links
          </h2>
          <div className="flex flex-col gap-8 py-8 max-w-screen-xl items-center justify-center">
            {links.map((link) => {
              return (
                <SecondaryButton
                  key={link.url}
                  Icon={link.icon}
                  onClick={() => {
                    window.open(link.url, "_blank");
                  }}
                >
                  {link.label}
                </SecondaryButton>
              );
            })}
          </div>
        </div>
      </section>
    </div>
  );
}
