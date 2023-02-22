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
  import CustomerForm from '../components/CustomerForm.vue'
  import EditCustomerForm from '../components/EditCustomerForm.vue'
  
  export default {
    components: { CustomerForm, EditCustomerForm },
  
    created() {
      this.getCustomers();
    },
  
    data() {
      return {
        dialog: false,
        customers: [],
        employees: [],
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
        customer_id: null,
        editDialog: false,
      }
      
    },
  
    computed: {
      totalPurchase() {
        return this.customers.reduce((acc, customer) => acc + Number(customer.purchase.replace(/[^0-9.-]+/g,"")), 0).toLocaleString('en-US', { style: 'currency', currency: 'AUD' })
      },
      
    },
    watch: {
      editDialog: function (val) {
        if (!val) {
          this.customer_id = null
        }
      }
    },
  
    methods: {

      async getCustomers() {
        this.employees = await this.$axios.$get('/employee/employees');
        this.customers = await this.$axios.$get('/customer/customers');

        let employeeLookup = this.employees.reduce((acc, employee) => {
          acc[employee.id] = employee.first_name + ' ' + employee.last_name;
          return acc;
        }, {});
       

        this.customers.forEach(customer => {
          customer.purchase = customer.purchase.toLocaleString('en-US', { style: 'currency', currency: 'AUD' })
          customer.employee_name = employeeLookup[customer.employee_id] || 'No Employee';
        })

      },
  
      async deleteCustomer(id) {
        await this.$axios.$delete('/customer/customer', { params: { id } })
        this.getCustomers()
      },
  
      async editCustomer(id) {
        this.customer_id = id
        this.editDialog = true
        
      },
    },
    
  }
  </script>