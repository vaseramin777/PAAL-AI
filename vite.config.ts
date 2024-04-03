import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Define a type for the Vite configuration
interface IViteConfig {
  plugins: react[]
}

// Export a default object that conforms to the IViteConfig type
export default defineConfig({
  plugins: [react()],
} as IViteConfig)
