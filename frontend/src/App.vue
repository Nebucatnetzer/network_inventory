<template>
  <div>
    <customer></customer>
    <the-footer></the-footer>
  </div>
</template>

<script>
import TheFooter from "./components/UI/TheFooter.vue";
import Customer from "./components/customers/Customers.vue";

export default {
  components: {
    TheFooter,
    Customer,
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
