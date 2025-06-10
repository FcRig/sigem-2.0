<template>
  <v-navigation-drawer v-model="drawer">
    <v-list nav>
      <v-list-item link to="/">
        <v-list-item-title>Home</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 'AppSidebar',
  data() {
    return { drawer: false };
  }
};
</script>
