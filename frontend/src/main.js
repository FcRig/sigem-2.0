import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';
import toasted from 'vue-toasted';
import './assets/styles.css';

const app = createApp(App);
app.use(router);
app.use(store);
app.use(vuetify);
app.use(toasted);
app.mount('#app');
