import { defineStore } from 'pinia'
import { useAuthStore } from './auth'

interface Project {
  id: number
  title: string
  description: string | null
  owner_id: number
  created_at: string
  updated_at: string
}

interface ProjectState {
  projects: Project[]
  loading: boolean
}

export const useProjectStore = defineStore('projects', {
  state: (): ProjectState => ({
    projects: [],
    loading: false,
  }),

  actions: {
    async fetchProjects() {
      const authStore = useAuthStore()
      this.loading = true

      const response = await fetch('http://localhost:8000/projects', {
        headers: {
          Authorization: `Bearer ${authStore.token}`,
        },
      })

      if (!response.ok) throw new Error('Failed to fetch projects')

      this.projects = await response.json()
      this.loading = false
    },

    async createProject(title: string, description: string) {
      const authStore = useAuthStore()

      const response = await fetch('http://localhost:8000/projects', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authStore.token}`,
        },
        body: JSON.stringify({ title, description }),
      })

      if (!response.ok) throw new Error('Failed to create project')

      const newProject = await response.json()
      this.projects.push(newProject)
      return newProject
    },

    async deleteProject(id: number) {
      const authStore = useAuthStore()

      const response = await fetch(`http://localhost:8000/projects/${id}`, {
        method: 'DELETE',
        headers: {
          Authorization: `Bearer ${authStore.token}`,
        },
      })

      if (!response.ok) throw new Error('Failed to delete project')

      this.projects = this.projects.filter(p => p.id !== id)
    },
  },
})