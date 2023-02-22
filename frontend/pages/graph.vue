<template>
    <div class="p-4 bg-white border border-gray-300 rounded-lg shadow-md">
      <h2 class="text-2xl font-bold mb-4 text-center">Customer Chart</h2>
      <div class="chart-container">
        <client-only>
          <BarChart :data="chartData" />
        </client-only>
      </div>
    </div>
  </template>

<script>
export default {
  data() {
    return {
      // An array of customer objects fetched from the server.
      customers: [],
    }
  },
  // Fetches the list of customers from the server when the component is created.
  created() {
    this.getCustomers()
  },
  methods: {
    // Fetches the list of customers from the server using an axios GET request.
    async getCustomers() {
      try {
        const response = await this.$axios.$get('/customer/customers')
        this.customers = response
      } catch (error) {
        console.error(error)
      }
    },
  },
  computed: {
    // Computes the chart data from the list of customers.
    chartData() {
      // Reduces the list of customers to a dictionary of purchase amounts keyed by purchase date.
      const purchaseData = this.customers.reduce((acc, customer) => {
        const purchaseDate = customer.purchase_date
        const purchaseAmount = customer.purchase

        if (!acc[purchaseDate]) {
          acc[purchaseDate] = purchaseAmount
        } else {
          acc[purchaseDate] += purchaseAmount
        }

        return acc
      }, {})

      // Sorts the purchase data by date.
      const sortedData = Object.entries(purchaseData).sort((a, b) => {
        return new Date(a[0]) - new Date(b[0])
      })

      // Extracts the labels and data from the sorted purchase data.
      const labels = sortedData.map(data => data[0])
      const data = sortedData.map(data => data[1])

      // Returns the chart data as an object with labels and datasets properties.
      return {
        labels: labels,
        datasets: [
          {
            label: 'Purchase Amount',
            data: data,
            backgroundColor: 'rgba(255, 153, 51, 0.3)', 
            borderColor: 'rgba(255, 102, 0, 1)',
            borderWidth: 2,
          },
        ],
      }
    },
  },
}
</script>

  
<style scoped>
.chart-container {
  position: relative;
  padding: 16px;
  border-radius: 4px;
}

.chart-container:before {
  content: "";
  display: block;
  padding-top: 75%;
}

.chart-container > * {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

@media (min-width: 640px) {
  .chart-container {
    padding: 32px;
    border: 2px solid #ddd;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  .chart-container:before {
    padding-top: 0;
  }

  .chart-container > * {
    position: static;
    width: auto;
    height: auto;
  }
}
</style>