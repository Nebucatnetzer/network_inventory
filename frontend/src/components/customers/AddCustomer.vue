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
          .then((response) => {
            this.$emit("created-customer", response.data);
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>

<style scoped>
dialog {
  margin: 0;
  position: fixed;
  top: 20vh;
  left: 30%;
  width: 40%;
  background-color: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 1rem;
}
label {
  font-weight: bold;
  display: block;
  margin-bottom: 0.5rem;
}

input,
textarea {
  display: block;
  width: 100%;
  font: inherit;
  padding: 0.15rem;
  border: 1px solid #ccc;
}
</style>
