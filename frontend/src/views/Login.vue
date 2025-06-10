<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card>
          <v-card-title class="text-h5">
            Sistema de Gestão do Núcleo de Multas - SIGEM
          </v-card-title>
          <v-card-text>
            <v-text-field label="Usuário" v-model="username" />
            <v-text-field label="Senha" v-model="password" type="password" />
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" @click="login">Entrar</v-btn>
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
