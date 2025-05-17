# # Use the official Bun image
# FROM oven/bun:1 as base
# WORKDIR /usr/src/app

# # Temp install için dev klasörü
# FROM base AS install
# RUN mkdir -p /temp/dev
# COPY package.json bun.lockb /temp/dev/
# RUN cd /temp/dev && bun install --frozen-lockfile

# # Prod bağımlılıkları için
# RUN mkdir -p /temp/prod
# COPY package.json bun.lockb /temp/prod/
# RUN cd /temp/prod && bun install --frozen-lockfile

# # Build aşaması
# FROM base AS prerelease
# COPY --from=install /temp/dev/node_modules /usr/src/app/node_modules
# COPY . /usr/src/app
# ENV NODE_ENV=production
# RUN bun --bun run build

# # Final image
# FROM base AS release
# WORKDIR /usr/src/app
# COPY --from=install /temp/prod/node_modules /usr/src/app/node_modules
# COPY --from=prerelease /usr/src/app/.output /usr/src/app/.output
# COPY package.json /usr/src/app/
# USER bun
# EXPOSE 3000/tcp
# ENV NUXT_HOST=0.0.0.0
# ENTRYPOINT ["sh", "-c", "bun run /usr/src/app/.output/server/index.mjs --host $NUXT_HOST"]
# Build Stage 1

# Base image olarak resmi Node.js slim kullan
FROM node:20-slim as base
WORKDIR /usr/src/app

# Sistem bağımlılıkları
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Geliştirme bağımlılıkları için ayrı katman
FROM base AS install
COPY package.json package-lock.json ./
RUN npm ci

# Build aşaması
FROM base AS build
COPY --from=install /usr/src/app/node_modules ./node_modules
COPY . .
ENV NODE_ENV=production
RUN npm run build

# Final imaj (sadece çıktılar ve prod modül)
FROM base AS release
WORKDIR /usr/src/app

# Yalnızca üretim bağımlılıklarını kopyala
COPY package.json package-lock.json ./
RUN npm ci --omit=dev

# Build çıktısını kopyala (önemli: .output dizini NGINX için gerekli)
COPY --from=build /usr/src/app/.output /usr/src/app/.output

# Opsiyonel: Config veya env varsa onları da kopyala
COPY --from=build /usr/src/app/.env /usr/src/app/.env
COPY --from=build /usr/src/app/nuxt.config.ts /usr/src/app/

EXPOSE 3000
ENV NUXT_HOST=0.0.0.0

# Nuxt'ün Node server modunda çalıştırılması
CMD ["node", ".output/server/index.mjs"]
