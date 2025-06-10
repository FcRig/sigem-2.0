<template>
  <v-app>
    <AppHeader :user="user" @logout="logout" />
    <AppSidebar />
    <v-main>
      <slot />
    </v-main>
    <AppFooter />
  </v-app>
</template>

<script>
import AppHeader from '../components/Header.vue';
import AppFooter from '../components/Footer.vue';
import AppSidebar from '../components/Sidebar.vue';
import { mapState } from 'vuex';

export default {
  name: 'MainLayout',
  components: { AppHeader, AppFooter, AppSidebar },
  computed: {
    ...mapState(['user'])
  },
  methods: {
    logout() {
      this.$store.commit('logout');
      this.$router.push('/login');
    }
  }
};
</script>

<!-- Move layout-specific styles here if needed -->
