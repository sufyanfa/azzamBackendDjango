/** @type {import('tailwindcss').Config} */ 
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors :{
        "primary": "#ABFA00",
        "secondary": "#4F00FA",
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}