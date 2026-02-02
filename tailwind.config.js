/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './core/templates/**/*.html',
    './**/templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        'brand-black': '#121212',
        'brand-white': '#FFFFFF',
        'brand-blue-1': '#196CFF',
        'brand-blue-2': '#29CFFF',
        'brand-dark': '#0A0A0A',
        'brand-gray': '#F5F5F7',
      },
      fontFamily: {
        'sans': ['Inter', 'sans-serif'], 
        'display': ['Outfit', 'sans-serif'],
      },
      animation: {
        'blob': 'blob 7s infinite',
      },
      keyframes: {
        blob: {
          '0%': { transform: 'translate(0px, 0px) scale(1)' },
          '33%': { transform: 'translate(30px, -50px) scale(1.1)' },
          '66%': { transform: 'translate(-20px, 20px) scale(0.9)' },
          '100%': { transform: 'translate(0px, 0px) scale(1)' },
        }
      }
    },
  },
  plugins: [],
}
