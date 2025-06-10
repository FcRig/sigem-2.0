<template>
  <v-app>
    <div class="grid-layout">
      <AppHeader :user="user" @logout="logout" class="header" />
      <AppSidebar class="sidebar" />
      <v-main class="content">
        <slot />
      </v-main>
      <AppFooter class="footer" />
    </div>
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

<style scoped>
.grid-layout {
  display: grid;
  min-height: 100vh;
  grid-template-rows: auto 1fr auto;
  grid-template-columns: 220px 1fr;
  grid-template-areas:
    "header header"
    "sidebar content"
    "footer footer";
}

.header {
  grid-area: header;
}

.sidebar {
  grid-area: sidebar;
}

.content {
  grid-area: content;
}

.footer {
  grid-area: footer;
}
</style>
