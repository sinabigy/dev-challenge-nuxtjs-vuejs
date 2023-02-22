<template>
  <v-app>
    <iframe id="my_iframe" style="display: none"></iframe>
    <!-- APP BAR -->
    <v-app-bar app color="deep-orange" dark>
      <router-link to="/">
      <v-toolbar-title class="ml-0 pl-3">
        <span class="font-weight-bold">Dev</span><span class="grey--text text--lighten-1">Challenge</span>
      </v-toolbar-title>
    </router-link>
      <v-btn text to="/employee">Employee</v-btn>
      <v-btn text to="/customer">Customer</v-btn>
      <v-btn text to="/graph">Graph</v-btn>
    </v-app-bar>

    <!-- CONTENT -->
    <v-main>
      <v-container fluid>
        <nuxt />
      </v-container>
    </v-main>

    <!-- FOOTER -->
    <v-footer app color="deep-orange" dark>
      <span class="white--text">&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {}
  },
  created() {},
  computed: {},
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro&display=swap');

// App bar
.v-app-bar__nav-icon {
  color: #fff;
}

// Footer
.v-footer {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50px;
}

// Global body styles
body {
  font-family: 'Source Code Pro', monospace;
  font-size: 16px;
  line-height: 1.5;
  color: #333;
}
</style>