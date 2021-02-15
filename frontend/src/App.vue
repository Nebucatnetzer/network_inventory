<template>
  <div>
    <the-customers></the-customers>
    <the-footer></the-footer>
  </div>
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
html {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
