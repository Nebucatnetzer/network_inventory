<template>
  <dialog open>
    <header><h1>Add Customer</h1></header>
    <form @submit.prevent="addCustomer">
      <label for="customer-name">Name</label>
      <input type="text" v-model.trim="customerName" id="customer-name" />
      <label id="customer-description">Description</label>
      <textarea
        v-model="customerDescription"
        id="customer-description"
      ></textarea>
      <div v-if="errorMessage">
        <p>You need to fill out both inputs.</p>
      </div>
      <button>Save</button>
    </form>
  </dialog>
</template>

<script>
import getAPI from "../scripts/axios-api";

export default {
  emits: ["created-customer"],
  data() {
    return {
      customerName: "",
      customerDescription: "",
      errorMessage: false,
    };
  },

  methods: {
    validateInput() {
      if (this.customerName === "") {
        this.errorMessage = true;
        return false;
      } else {
        return true;
      }
    },
    addCustomer() {
      if (this.validateInput()) {
        getAPI
          .post("/customers/", {
            name: this.customerName,
            description: this.customerDescription,
          })
          .then(function(response) {
            this.$emit("close", response.data);
          })
          .catch(function(error) {
            console.log(error);
          });
      }
    },
  },
};
</script>

<style></style>
