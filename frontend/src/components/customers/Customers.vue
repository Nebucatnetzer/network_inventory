<template>
  <header><h1>List of Customers</h1></header>
  <div>
    <form @submit.prevent="addCustomer">
      <input type="submit" value="Add Customer" class="btn btn-primary" />
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

    <tr v-for="customer in customers" :key="customer.id">
      <td>
        <a href="">{{ customer.name }}</a>
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
</template>

<script>
import getAPI from "../scripts/axios-api";

export default {
  data() {
    return {
      customers: [],
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
