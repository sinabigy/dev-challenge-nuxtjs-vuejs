<template>
    <v-container class="py-12" fluid>
      <v-snackbar v-model="snackbar" :color="'deep-orange accent-4'">
        <span class="white--text">Welcome to Dev Challenge!</span>
        <v-btn color="white" text @click="snackbar = false">Close</v-btn>
      </v-snackbar>
      <v-parallax height="300" src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg">
        <h1 class="text-h3 text-center mb-12">Dev Challenge</h1>
      </v-parallax>
      <v-divider class="pb-10"></v-divider>
      <v-row justify="center">
        <v-col cols="12" md="4">
          <v-card color="deep-orange darken-3" class="white--text" hover>
            <v-card-title>
              <v-icon size="48" color="white">mdi-account-multiple</v-icon>
              <span class="text-h4">Employees</span>
            </v-card-title>
            <v-card-text>
              <p class="text-caption">View and manage employees.</p>
            </v-card-text>
            <v-card-actions>
              <v-btn color="white" href="/employee">View Employees</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="12" md="4">
          <v-card color="deep-orange darken-3" class="white--text" hover>
            <v-card-title>
              <v-icon size="48" color="white">mdi-account</v-icon>
              <span class="text-h4">Customers</span>
            </v-card-title>
            <v-card-text>
              <p class="text-caption">View and manage customers.</p>
            </v-card-text>
            <v-card-actions>
              <v-btn color="white" href="/customer">View Customers</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="12" md="4">
          <v-card color="deep-orange darken-3" class="white--text" hover>
            <v-card-title>
              <v-icon size="48" color="white">mdi-chart-line</v-icon>
              <span class="text-h4">Graphs</span>
            </v-card-title>
            <v-card-text>
              <p class="text-caption">View analytics and insights.</p>
            </v-card-text>
            <v-card-actions>
              <v-btn color="white" href="/graph">View Graphs</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>

  
<script>
export default {
  data() {
    return {
      snackbar: {
        show: false,
        timeout: 10000,
        color: "info",
        text: "Welcome to the Dev Challenge page!",
      },
    };
  },
  mounted() {
    // Shows the snackbar notification when the component is mounted.
    this.snackbar.show = true;
  },
};
</script>

  <style lang="scss">
  @import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro&display=swap');
  
  * {
    font-family: 'Source Code Pro', monospace !important;
  }
  
  h1 {
    font-size: 2.5rem;
    font-weight: 600;
  }
  
  .text-h3 {
    font-size: 1.875rem;
    font-weight: 600;
  }
  
  .text-h4 {
    font-size: 1.5rem;
    font-weight: 600;
  }
  
  .text-caption {
    font-size: 0.875rem;
    font-weight: 400;
    line-height: 1.375rem;
  }
  

  
  .v-card__title {
    line-height: 1.25rem;
  }
  </style>