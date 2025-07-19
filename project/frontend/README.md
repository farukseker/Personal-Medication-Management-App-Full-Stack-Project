# Nuxt Minimal Starter

npx nuxt dev --host 192.168.123.97 --port 4080 --https --ssl-cert .ssl/192.168.123.97.pem --ssl-key .ssl/192.168.123.97-key.pem


chrome://inspect#devices


Look at the [Nuxt documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

## Setup

Make sure to install dependencies:

```bash
# npm
npm install

# pnpm
pnpm install

# yarn
yarn install

# bun
bun install
```

## Development Server

Start the development server on `http://localhost:3000`:

```bash
# with ssl via NUXT
npx nuxt dev --https --ssl-cert .ssl/localhost.pem --ssl-key .ssl/localhost-key.pem

# npm
npm run dev

# pnpm
pnpm dev

# yarn
yarn dev

# bun
bun run dev
```

## Production

Build the application for production:

```bash
# npm
npm run build

# pnpm
pnpm build

# yarn
yarn build

# bun
bun run build
```

Locally preview production build:

```bash
# npm
npm run preview

# pnpm
pnpm preview

# yarn
yarn preview

# bun
bun run preview
```

Check out the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.
