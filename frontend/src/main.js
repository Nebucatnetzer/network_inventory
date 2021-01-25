import { createApp } from "vue";

import App from "./App.vue";
import Customer from "./components/Customers.vue";
import "./index.css";

const app = createApp(App);
app.component("customer", Customer);
app.mount("#app");
