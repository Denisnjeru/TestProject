<!-- <template>
  <div class="home page-container">
    <div class="page">
      <h4 class="page__title">Dashboard</h4>

        {{dashboard.monthly_earning}}
      <div class="page__content">
        <div class="main">
          <div class="statistics">
            <div class="statistics__item unique">
              <doughnut-chart :width="100" :values="pieChartData" :height="100" :key="showPieChart"></doughnut-chart>
              <ul class="chart-labels">
                <li class="chart-label"><font-awesome-icon class="color-icon total" icon="circle" /> Ordered - {{dashboard.ordered  | toCurrency('Ksh')}}</li>
                <li class="chart-label"><font-awesome-icon class="color-icon spent" icon="circle" /> Delivered - {{dashboard.delivered  | toCurrency('Ksh')}}</li>
                <li class="chart-label"><font-awesome-icon class="color-icon balance" icon="circle" /> Invoiced - {{dashboard.invoiced  | toCurrency('Ksh')}}</li>
              </ul>
            </div>
            <div class="statistics__item info">
              <p class="desc">{{dashboard.total_purchase_orders}}</p>
              <p class="title">Purchase Orders</p>
              <ul class="list">
                <li class="list__item">Delivered - {{dashboard.total_purchase_orders_delivered}}</li>
                <li class="list__item">Pending - {{dashboard.total_purchase_orders_pending}}</li>
              </ul>
            </div>
            <div class="statistics__item info">
              <p class="desc">{{dashboard.total_invoices}}</p>
              <p class="title">Invoices</p>
              <ul class="list">
                <li class="list__item">Approved - {{dashboard.total_invoices_approved}}</li>
                <li class="list__item">Pending - {{dashboard.total_invoices_pending}}</li>
              </ul>
            </div>
          </div>
          <div class="spend-line-graph">
            <p class="tab-title">Monthly PO's and Invoices</p>
            <multi-line-chart v-if="lineChartDataPO.length > 0" :height="300" :valuesA="lineChartDataPO" labelA="PO" :valuesB="lineChartDataInvoice" labelB="Invoice" stepSize="20" :dates="dates"></multi-line-chart>
          </div>
        </div>
        <div class="side">
          <div class="side__item spend-pie-chart">
            <p class="title">Pending Actions</p>
            <ul class="list">
              <li class="list__item"><font-awesome-icon class="icon" icon="circle" />Update invoice <span class="link">#I001</span></li>
              <li class="list__item"><font-awesome-icon class="icon" icon="circle" />Acknowledge PO <span class="link">#P0012</span></li>
            </ul>
          </div>
          <div class="side__item approval-requests">
            <p class="title">Recent Activity</p>
            <ul class="list">
              <li class="list__item"><font-awesome-icon class="icon" icon="circle" />Invoice approved <span class="link">#I001</span></li>
              <li class="list__item"><font-awesome-icon class="icon" icon="circle" />PO acknowledged <span class="link">#P001</span></li>
            </ul>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import MultiLineChart from '@/components/charts/budget/MultiLineChart'
import DoughnutChart from '@/components/charts/budget/DoughnutChart'
import supplier_portal from '@/services/supplier_portal'
export default {
  name: 'home',
  data () {
    return {
      dates: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      values: [600,	1150,	342,	6050,	2522,	3241,	1259,	157,	1545, 9841,],
      lineChartDataPO: [],
      lineChartDataInvoice: [],
      stepSize: 2000,
      pieChartData: [],
      dashboard: {},
      showPieChart: false
    }
  },
  components: {
    MultiLineChart,
    DoughnutChart
  },
  mounted() {
    this.getDashboard()
  },
  methods: {
    async getDashboard() {
      try {
        const response = await supplier_portal.dashboard()
        this.dashboard = response.data
        this.pieChartData.push(this.dashboard.ordered)
        this.pieChartData.push(this.dashboard.delivered)
        this.pieChartData.push(this.dashboard.invoiced)
        this.showPieChart = !this.showPieChart

        let monthly_earnings = this.dashboard.monthly_earnings
        this.lineChartDataPO = monthly_earnings.map(a => a.po)
        this.lineChartDataInvoice = monthly_earnings.map(a => a.invoice)
        let maxSpend1 = Math.max.apply(Math, monthly_earnings.map(function(o) { return o.po; }))
        this.stepSize = Math.ceil((maxSpend1/8)/100)*100
      } catch (err) {
        console.log(err)
      }
    },
  }

}
</script>

<style lang="scss" scoped>

.page {
  width: 100%;

  &__content {
    @include grid_row;
    align-items: flex-start;
    padding: $line-height/1.5 0;
  }

  .main {
    width: 78%;
    height: auto;
    padding: 0;
  }

  .side {
    width: 20%;
    height: auto;
  }
}

.main {
  .statistics {
    width: 100%;
    @include grid_row;
    padding: 0 2%;

    &__item {
      width: 30%;
      height: 20vh;
      // background-color: $color-white-milk;
      // border-radius: $line-height/3;
      @include shadow;
      // border: 1px solid $color-white-milk;
    }

    .unique {
      @include grid_row;
      justify-content: center;
      width: 40%;

      .chart-labels {
        margin-left: $line-height;

        .chart-label {
          font-size: $font-size-small;
          padding: $line-height/6 0;
          font-weight: 600;

          .color-icon {
            font-size: $line-height/3;
          }

          .total {
            color: rgba(255,99,132,1);
          }

          .spent {
            color: rgba(54, 162, 235, 1);
          }

          .balance {
            color: rgba(255, 206, 86, 1);
          }
        }
      }
    }

    .info {
      @include grid_column;
      justify-content: center;
      align-items: center;
      width: 25%;

      .title {
        font-weight: 600;
        font-size: $font-size-text;
        margin-bottom: $line-height/3;
      }

      .desc {
        padding: $line-height/4 0;
        font-weight: 600;
        font-size: $line-height*0.8;
        color: $color-green-main;
      }

      .list {
        &__item {         
          font-size: $font-size-small;
          padding: $line-height/8 0;
          color: $color-gray-medium;

          &:first-child {
            padding-top: 0;
          }
        }
      }
    }
  }

  .spend-line-graph {
    width: 96%;
    // background-color: $color-white-milk;
    // border-radius: $line-height/3;
    // @include shadow;
    height: auto;
    margin: $line-height 2%;
    // border: 1px solid $color-white-milk;
    padding: $line-height $line-height/3;
  }
}

.side {
  .spend-pie-chart {
    width: 92%;
    height: 30vh;
    margin: 0 4%;
    // border-radius: $line-height/3;
    // border: 1px solid $color-white-milk;
    background-color: $color-white-milk;
    @include shadow;
  }

  .approval-requests {
    width: 92%;
    height: 40vh;
    margin: $line-height 4%;
    // border-radius: $line-height/3;
    background-color: $color-blue-main;
    @include shadow;
  }

  &__item {
    padding: $line-height/2;

    .title {
      padding: $line-height/4 0;
      font-weight: 600;
      font-size: $font-size-small;
    }

    .list {
      margin-top: $line-height/4;
      &__item {
        font-size: $font-size-small;
        padding: $line-height/10 0;

        .icon {
          font-size: $font-size-small;
          padding: 0 $line-height/6;
        }

        .link {
          color: $color-blue-light;
          font-weight: 600;
          cursor: pointer;
        }
      }
    }
  }

  .spend-pie-chart {
    .title {
      color:$color-blue-main;
    }    
  }

  .approval-requests {
    .title {
      color: $color-blue-light;
    }

    .list__item {
      color: $color-white-milk;

      .link {
        color: $color-green-main;
      }
    }
  }
}

.tab-title {
  text-align: center;
  margin: $line-height/2 0;
  font-weight: 600;
  font-size: $font-size-small;
}
</style> -->
