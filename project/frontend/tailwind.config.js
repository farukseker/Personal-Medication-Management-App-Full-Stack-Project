/** @type {import('tailwindcss').Config} */
export default {
  content: [],
  darkMode: 'class',
  theme: {
    container: {
      center: true,
    },
    extend: {
      dropShadow: {
        'white-glow': '0 0 10px rgba(255, 255, 255, 0.8)',
      },
      fontFamily: {
        enTurk: ['Noto Sans Old Turkic', 'serif'],
      },
    },
  },
  plugins: [require('daisyui')],
  daisyui: {
    themes: ["light", "dark"], // sadece light ve dark aktif
  },
}

