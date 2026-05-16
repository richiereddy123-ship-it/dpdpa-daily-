import type { Config } from "tailwindcss";
const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sora: ["Sora", "sans-serif"],
        dm: ["DM Sans", "sans-serif"],
      },
      colors: {
        brand: {
          DEFAULT: "#0F6E56",
          light: "#1D9E75",
          muted: "#E1F5EE",
        },
      },
    },
  },
  plugins: [],
};
export default config;
