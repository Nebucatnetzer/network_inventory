<template>
  <the-customers></the-customers>
  <the-footer></the-footer>
</template>

<script>
import TheFooter from "./components/UI/TheFooter.vue";
import TheCustomers from "./components/customers/TheCustomers.vue";

export default {
  components: {
    TheFooter,
    TheCustomers,
  },
  data() {
    return {};
  },
};
</script>

<style>
* {
  box-sizing: border-box;
}
html {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.card {
  margin: 2rem auto;
  max-width: 40rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 2rem;
  background-color: #ffffff;
}
button {
  font: inherit;
  border: 1px solid #0076bb;
  background-color: #0076bb;
  color: white;
  cursor: pointer;
  padding: 0.75rem 2rem;
  border-radius: 30px;
}
</style>
