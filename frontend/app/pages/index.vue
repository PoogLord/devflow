<template>
  <div></div>
</template>

<script setup lang="ts">
import { useAuthStore } from '../stores/auth'

onMounted(() => {
  const authStore = useAuthStore()
  if (authStore.isAuthenticated) {
    navigateTo('/dashboard')
  } else {
    navigateTo('/login')
  }
})
</script>