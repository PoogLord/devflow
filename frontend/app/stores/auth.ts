import { defineStore } from 'pinia'

interface User {
  id: number
  email: string
  username: string
  is_active: boolean
  created_at: string
}

interface AuthState {
  user: User | null
  token: string | null
}

export const useAuthStore = defineStore('auth', {
  state: (): AuthState => ({
    user: null,
    token: null,
  }),

  getters: {
    isAuthenticated: (state) => !!state.token,
  },

  actions: {
    async register(email: string, username: string, password: string) {
      const response = await fetch('http://localhost:8000/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, username, password }),
      })

      if (!response.ok) {
        const error = await response.json()
        throw new Error(error.detail)
      }

      return await response.json()
    },

    async login(email: string, password: string) {
      const response = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, username: email, password }),
      })

      if (!response.ok) {
        const error = await response.json()
        throw new Error(error.detail)
      }

      const data = await response.json()
      this.token = data.access_token
      localStorage.setItem('token', data.access_token)
    },

    logout() {
      this.user = null
      this.token = null
      localStorage.removeItem('token')
      navigateTo('/login')
    },
  },
})