// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: {
    enabled: true,

    timeline: {
      enabled: true,
    },
  },
  ssr: false,
    routeRules: {
    '/': {
      headers: {
        'x-nuxt-override': 'true'
      }
    }
  },
  app: {
    head: {
      link: [
        {
          rel: 'manifest',
          href: '/manifest.webmanifest',
        },
      ],
    },
  },
  modules: [
    '@nuxt/ui',
    '@nuxtjs/tailwindcss',
    '@vesp/nuxt-fontawesome',
    '@nuxt/content',
    '@nuxtjs/mdc',
    '@nuxtjs/google-fonts',
    '@pinia/nuxt',
    '@nuxt/image',
    'vue3-carousel-nuxt',
    '@vueuse/motion/nuxt',
    '@vite-pwa/nuxt',
    '@nuxtjs/color-mode'
  ],
    colorMode: {
    classSuffix: '',
    preference: 'light',
    fallback: 'light',
  },
  // pwa: {
  //   registerType: 'autoUpdate',
  //   manifest: {
  //     name: 'Uygulama Adı',
  //     short_name: 'Kısa Ad',
  //     description: 'Uygulamanızın açıklaması',
  //     theme_color: '#ffffff',
  //     icons: [
  //       {
  //         src: '/icon-192x192.png',
  //         sizes: '192x192',
  //         type: 'image/png',
  //       },
  //       {
  //         src: '/icon-512x512.png',
  //         sizes: '512x512',
  //         type: 'image/png',
  //       },
  //     ],
  //   },
    
  // },
  mdc: {
    components: {
      map: {
        carousel: 'Carousel',
        custom: 'CustomField', // `[custom][/custom]` için özel bir bileşen tanımlayın,
        moni: 'Moni'
      },
    },
  },
  image: {
    domains: ['public.blob.vercel-storage.com'],
  },
  css: [
    '@/assets/css/tailwind.css',
  ],
  plugins: [
    // '~/plugins/heatmap.client.ts'
  ],
  fontawesome: {
    icons: {
      solid: ['coffee', 'child',],
      regular: ['comment',],
      brands: ['twitter', 'Instagram',],
    }
  },
  vite: {
    optimizeDeps: {
      include: ['debug']
    }
  },
  // vue: {
  //   compilerOptions: {
  //     isCustomElement: (tag) => tag === 'MDC', // Özel MDC öğesini belirtin
  //   },
  // },
  googleFonts: {
    families: {
      'Nunito': [400, 500, 600, 700],
      'Roboto': [400, 500, 700],
      'Ubuntu': [400, 500, 700],
      'Noto Sans Old Turkic': [400],
    },
  },
  runtimeConfig: {
    API_HOST: process.env.NUXT_API_PATH,
    public: {
      API_HOST: process.env.NUXT_API_PATH,
    }
  },

})