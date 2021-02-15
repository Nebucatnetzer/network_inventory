<template>
  <customer-details
    v-if="showCustomerDetails"
    :customer-name="customerName"
    :customer-description="customerDescription"
    @hide-details="hideDetails"
  ></customer-details>

  <add-customer
    v-if="addCustomerDialogVisible"
    @created-customer="closeDialog"
  ></add-customer>

  <div v-if="!addCustomerDialogVisible && !showCustomerDetails" class="card">
    <header><h1>List of Customers</h1></header>
    <div>
      <form @submit.prevent="addCustomer">
        <button>Add Customer</button>
      </form>
    </div>
    <table class="table table-hover table-bordered">
      <tr>
        <th class="orderable">Name</th>
        <th>Nets</th>
        <th>Computers</th>
        <th>Devices</th>
        <th>Backups</th>
        <th>Licenses</th>
        <th>Users</th>
        <th>Actions</th>
      </tr>

      <tr v-for="customer in customers" :key="customer.url">
        <td>
          <a href="#" @click="showDetails(customer)">{{ customer.name }}</a>
        </td>
        <td><a :href="customer.url">Nets</a></td>
        <td><a :href="customer.url">Computers</a></td>
        <td><a :href="customer.url">Devices</a></td>
        <td><a :href="customer.url">Backups</a></td>
        <td><a :href="customer.url">Licenses</a></td>
        <td><a :href="customer.url">Users</a></td>
        <td>
          <a href="#" @click="deleteCustomer(customer.url)">delete</a>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import getAPI from "../scripts/axios-api";
import AddCustomer from "./AddCustomer.vue";
import CustomerDetails from "./CustomerDetails.vue";

export default {
  components: {
    AddCustomer,
    CustomerDetails,
  },
  data() {
    return {
      customers: [],
      addCustomerDialogVisible: false,
      showCustomerDetails: false,
      customerName: "",
      customerDescription: "",
    };
  },
  methods: {
    deleteCustomer(url) {
      getAPI
        .delete(url)
        .then(() => {
          this.customers = this.customers.filter(
            (customer) => customer.url !== url
          );
        })
        .catch((err) => {
          console.log(err);
        });
    },
    addCustomer() {
      this.addCustomerDialogVisible = true;
    },
    closeDialog(customer) {
      this.customers.unshift(customer);
      this.addCustomerDialogVisible = false;
    },
    showDetails(customer) {
      this.customerName = customer.name;
      this.customerDescription = customer.description;
      this.showCustomerDetails = true;
    },
    hideDetails() {
      this.showCustomerDetails = false;
    },
  },
  created() {
    getAPI
      .get("/customers/")
      .then((response) => {
        this.customers = response.data.results;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>
