// https://vite.dev/config/

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const basePath = '/'
// const basePath = '/test_python/'

export default defineConfig({
  base: basePath,
  plugins: [vue()],
})
