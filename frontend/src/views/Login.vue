<template>
  <v-container class="fill-height login-page" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card class="login-card" elevation="8" rounded="lg" color="white">
          <v-card-title class="text-h5 prf-title text-center">
            Sistema de Gestão do Núcleo de Multas - SIGEM
          </v-card-title>
          <v-card-text>
            <v-text-field
              class="mb-4"
              label="Usuário"
              v-model="username"
              prepend-inner-icon="mdi-account"
            />
            <v-text-field
              class="mb-4"
              label="Senha"
              v-model="password"
              type="password"
              prepend-inner-icon="mdi-lock"
            />
          </v-card-text>
          <v-card-actions>
            <v-btn color="secondary" @click="login" dark>Entrar</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return { username: '', password: '' };
  },
  methods: {
    login() {
      this.$store.commit('setUser', { name: this.username });
      this.$router.push('/');
    }
  }
};
</script>

<style scoped>
.login-page {
  background: linear-gradient(135deg, #002776, #001a4d);
  color: #fff;
}

.login-card {
  max-width: 500px;
  border-top: 4px solid #FFCC00;
}

.prf-title {
  color: #002776;
}
</style>
