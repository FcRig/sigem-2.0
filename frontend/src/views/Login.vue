<template>
  <v-app>
    <v-main class="fill-height">
      <v-container fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4">
            <v-card class="pa-6 rounded-lg elevation-8">
              <div class="logo-container">
                <img
                  src="https://auto.prf.gov.br/assets/logo-PRF.8d8f70ac.svg"
                  alt="Logo PRF"
                  class="logo"
                >
              </div>

              <v-card-title class="text-h6 text-center mb-4">
                Sistema de Gestão do Núcleo de Multas – SIGEM
              </v-card-title>

              <v-form>
                <v-text-field
                  v-model="cpf"
                  label="CPF"
                  prepend-inner-icon="mdi-account"
                  maxlength="14"
                  outlined
                  hide-details
                  class="mb-4"
                ></v-text-field>

                <v-text-field
                  v-model="senha"
                  label="Senha"
                  prepend-inner-icon="mdi-lock"
                  type="password"
                  outlined
                  hide-details
                  class="mb-6"
                ></v-text-field>

                <v-btn color="primary" block class="mb-2" @click="login">
                  Entrar
                </v-btn>

                <v-btn color="secondary" variant="text" block>
                  Esqueci minha senha
                </v-btn>
              </v-form>

              <v-card-subtitle class="text-center mt-6 caption">
                © {{ year }} Polícia Rodoviária Federal
              </v-card-subtitle>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref, computed } from 'vue'

const cpf = ref('')
const senha = ref('')
const year = new Date().getFullYear()

function login() {
  // lógica de autenticação aqui
  console.log({ cpf: cpf.value, senha: senha.value })
}
</script>

<style scoped>
.fill-height {
  min-height: 100vh;
  background: #e4e5e6;
}

.logo-container {
  display: flex;
  justify-content: center;
  margin-bottom: 24px;
}

.logo {
  width: 140px;
  height: auto;
}
</style>
