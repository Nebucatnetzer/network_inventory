import Vue from 'vue'
import VueRouter from 'vue-router'
import Customers from './views/Customers'


Vue.use(VueRouter)

export default new VueRouter({
    history: 'history',
    base: process.env.BASE_URL,
    routes: [{
        path: '/',
        name: 'customers',
        component: Customers,
    }, ]
})
