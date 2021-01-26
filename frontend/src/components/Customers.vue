<template>
    <div class="row">
        <div class="col">
            <div class="table-container">
                <table class="table table-hover table-bordered">
                    <tr>
                        <th class="orderable">Customer</th>
                        <th>Description</th>
                    </tr>
                    <tr v-for="customer in customers" :key="customer.id">
                        <td>
                            {{ customer.name }}
                        </td>
                        <td>{{ customer.description }}</td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import { getAPI } from "../axios-api";

export default {
    data() {
        return {
            customers: [],
        };
    },
    created() {
        getAPI
            .get("/customers/")
            .then((response) => {
                console.log("Post API has recieved data");
                this.customers = response.data.results;
            })
            .catch((err) => {
                console.log(err);
            });
    },
};
</script>
