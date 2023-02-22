<template>
  <v-card>
    <v-card-title> Add Customer </v-card-title>
    <v-card-text>
      <v-form ref="form">
        <v-text-field v-model="customer.first_name" label="First Name" :rules="nameRules" />
        <v-text-field v-model="customer.last_name" label="Last Name" :rules="nameRules" />
        <v-text-field v-model="customer.email" label="Email" :rules="emailRules" />
        <v-text-field v-model="customer.purchase" label="Purchase Amount" :rules="purchaseRules" />
        <v-select v-model="customer.employee_id" :items="employees" label="Employee ID" />
        <v-menu
          ref="menu"
          v-model="menu"
          :close-on-content-click="false"
          :nudge-right="40"
          :return-value.sync="customer.purchase_date"
          transition="scale-transition"
          offset-y
          min-width="auto"
        >
          <template v-slot:activator="{ on }">
            <v-text-field
              v-model="formattedDateTime"
              label="Purchase Date"
              append-icon="mdi-calendar"
              :readonly="true"
              v-on="on"
            />
          </template>
          <v-date-picker v-model="customer.purchase_date" no-title scrollable>
            <v-spacer></v-spacer>
            <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
            <v-btn text color="primary" @click="$refs.menu.save(customer.purchase_date)">OK</v-btn>
          </v-date-picker>
        </v-menu>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-btn :disabled="lock" @click="addCustomer()" color="primary">Save</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ["customer_id"],
  data() {
    return {
      // Defines the customer object with initial values for each field.
      customer: {
        first_name: "",
        last_name: "",
        email: "",
        purchase: "",
        purchase_date: "",
        employee_id: "",
      },
      // An array of employee objects used to populate the employee select field.
      employees: [],
      // Controls the visibility of the purchase date picker.
      menu: false,
      // Controls whether the save button is disabled or not.
      lock: false,
      // The formatted date string displayed in the purchase date text field.
      formattedDateTime: "",
      // Validation rules for the first and last name text fields.
      nameRules: [v => !!v || "Name is required"],
      // Validation rules for the email text field.
      emailRules: [
        v => !!v || "E-mail is required",
        v => /.+@.+\..+/.test(v) || "E-mail must be valid",
      ],
      // Validation rules for the purchase amount text field.
      purchaseRules: [
        v => !!v || "Purchase amount is required",
        v => /^\d+(\.\d{1,2})?$/.test(v) || "Purchase amount must be a valid number",
      ],
    };
  },
  // A watcher that updates the formattedDateTime property when the customer.purchase_date property changes.
  watch: {
    'customer.purchase_date': function(val) {
      this.formattedDateTime = this.formatDate(new Date(val));
    },
  },
  methods: {
    // Formats a Date object as a string in the format YYYY-MM-DD.
    formatDate(date) {
      const year = date.getFullYear();
      const month = ('0' + (date.getMonth() + 1)).slice(-2);
      const day = ('0' + date.getDate()).slice(-2);
      return `${year}-${month}-${day}`;
    },
    // Submits a POST request to the server to add a new customer.
    async addCustomer() {
      // Validates the form before submitting the request.
      if (this.$refs.form.validate()) {
        this.lock = true;
        await this.$axios.$post("/customer/customer", this.customer);
        this.lock = false;
        // Resets the customer object to its initial values.
        this.customer = {
          first_name: "",
          last_name: "",
          email: "",
          purchase: "",
          purchase_date: "",
          employee_id: "",
        };
        // Emits a 'save' event to notify the parent component that a new customer was added.
        this.$emit("save");
      }
    },
  },
  // Initializes the component by fetching the list of employees from the server and mapping them to an array of objects that can be used to populate the employee select field.
  async created() {
    this.employees = await this.$axios.$get("/employee/employees");
    this.employees = this.employees.map((employee) => {
      return {
        text: `${employee.first_name} ${employee.last_name}`,
        value: employee.id,
      };
    });
  },
};
</script>