import type { Config } from "tailwindcss";
import daisyui from "daisyui";

const config: Config = {
    content: [
    './components/**/*.{vue,js,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './plugins/**/*.js',
    './nuxt.config.{js,ts}',
  ],
  plugins: [daisyui({themes:'all'})],
}

export default config;
