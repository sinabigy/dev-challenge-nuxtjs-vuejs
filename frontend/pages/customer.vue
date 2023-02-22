<template>
   
    <v-card>
      <v-card-title>
        Customer List
        <v-btn icon @click="dialog = true">
          <v-icon>mdi-plus</v-icon>
        </v-btn>
      </v-card-title>
      <v-data-table :headers="headers" :items="customers">
        <template v-slot:item.active="{ item }">
          <v-btn icon class="mr-2" @click="deleteCustomer(item.id)">
            <v-icon>mdi-delete</v-icon>
          </v-btn>
          <v-btn icon @click="editCustomer(item.id)">
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
        </template>

        
        <template v-slot:footer >
            <v-divider></v-divider>
            <!-- // put text to the rightk -->
            <v-col cols="12" class="text-right">
              Total Purchase: {{ totalPurchase }}
              
            </v-col>

        </template>

      </v-data-table>
  
      <v-dialog v-model="dialog">
        <customer-form @save="dialog = false; getCustomers()" />
      </v-dialog>
  
      <v-dialog v-model="editDialog">
        <edit-customer-form :customer_id="customer_id" @save="editDialog = false; getCustomers()" />
      </v-dialog>
    </v-card>
    
  </template>

  
<script>
// import CustomerForm and EditCustomerForm components from their respective files
import CustomerForm from '../components/CustomerForm.vue'
import EditCustomerForm from '../components/EditCustomerForm.vue'

export default {
  // register CustomerForm and EditCustomerForm components
  components: { CustomerForm, EditCustomerForm },
  
  // fetch customers data when the component is created
  created() {
    this.getCustomers();
  },

  data() {
    // define the component's data properties
    return {
      // dialog state for adding a new customer
      dialog: false,
      // list of all customers
      customers: [],
      // list of all employees
      employees: [],
      // table headers for displaying customer data
      headers: [
        { text: 'First Name', value: 'first_name' },
        { text: 'Last Name', value: 'last_name' },
        { text: 'Email', value: 'email' },
        { text: 'Purchase Amount', value: 'purchase' },
        { text: 'Purchase Date', value: 'purchase_date' },
        { text: 'Employee ID', value: 'employee_id' },
        { text: 'Employee Name', value: 'employee_name'},
        { text: 'Actions', value: 'active', sortable: false },
      ],
      // the ID of the customer being edited
      customer_id: null,
      // dialog state for editing a customer
      editDialog: false,
    }
  },

  computed: {
    // compute the total purchase amount of all customers
    totalPurchase() {
      return this.customers.reduce((acc, customer) => acc + Number(customer.purchase.replace(/[^0-9.-]+/g,"")), 0).toLocaleString('en-US', { style: 'currency', currency: 'AUD' })
    },
  },

  watch: {
    // set customer_id to null when the edit dialog is closed
    editDialog: function (val) {
      if (!val) {
        this.customer_id = null
      }
    }
  },

  methods: {
    // fetch customers and employees data from the server
    async getCustomers() {
      this.employees = await this.$axios.$get('/employee/employees');
      this.customers = await this.$axios.$get('/customer/customers');

      // create a lookup table for employees
      let employeeLookup = this.employees.reduce((acc, employee) => {
        acc[employee.id] = employee.first_name + ' ' + employee.last_name;
        return acc;
      }, {});

      // format purchase amount and employee name for each customer
      this.customers.forEach(customer => {
        customer.purchase = customer.purchase.toLocaleString('en-US', { style: 'currency', currency: 'AUD' })
        customer.employee_name = employeeLookup[customer.employee_id] || 'No Employee';
      })
    },

    // delete a customer from the server
    async deleteCustomer(id) {
      await this.$axios.$delete('/customer/customer', { params: { id } })
      this.getCustomers()
    },

    // open the edit dialog for a customer
    async editCustomer(id) {
      this.customer_id = id
      this.editDialog = true
    },
  },
}
</script>