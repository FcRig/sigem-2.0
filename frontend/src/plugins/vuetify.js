import { createVuetify } from 'vuetify';
import 'vuetify/styles';

export default createVuetify({
  theme: {
    defaultTheme: 'customLight',
    themes: {
      customLight: {
        dark: false,
        colors: {
          primary: '#1976D2',
          secondary: '#424242',
          accent: '#82B1FF'
        }
      }
    }
  }
});
