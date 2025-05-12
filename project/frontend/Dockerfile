# Base image olarak Node.js kullanıyoruz
FROM node:22.13.1

# Çalışma dizinini oluştur ve ayarla
WORKDIR /app

# package.json ve package-lock.json dosyalarını kopyala
COPY package*.json ./

ENV NUXT_API_PATH="https://api.farukseker.com.tr/api"

# Bağımlılıkları yükle
RUN npm install

# Nuxt.js hazırlık komutunu çalıştır
RUN npm run postinstall

# Uygulama dosyalarını kopyala
COPY . .

# Nuxt.js uygulamasını build et
RUN npm run build

# Uygulamanın çalışacağı portu tanımla
EXPOSE 3000

# Uygulamayı başlat
CMD ["npm", "run", "preview"]
