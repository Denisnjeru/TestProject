<template>
  <div class="home page-container">
    <div class="page">
      <h4 class="page__title">Dashboard</h4>
      <div class="page__content">
        <div class="main">
          <div class="filter">
            
          </div>
          <div class="statistics">
            <div class="statistics__item unique">
              
              <p class="title">Approval Requests</p>
              <span class="graph">
                <doughnut-chart :width="100" :values="pieChartData" :height="100"></doughnut-chart>                        
                <ul class="chart-labels">
                  <li class="chart-label"><font-awesome-icon class="color-icon total" icon="circle" /> Total - 0</li>
                  <li class="chart-label"><font-awesome-icon class="color-icon spent" icon="circle" /> Approved - 0</li>
                  <li class="chart-label"><font-awesome-icon class="color-icon balance" icon="circle" /> Pending - 0</li>
                </ul>
              </span>    
            </div>
            <div class="statistics__item info">
              <p class="desc pos">1</p>
              <p class="title">Purchase Orders</p>
              <AreaLineChartApex chartTitle="1 Purchase Orders" :chartHeight="30" :values="values" :months="months" color="#56caf0"/>
            </div>
            <div class="statistics__item info">
              <p class="desc">0</p>
              <p class="title">Invoices</p>
              <AreaLineChartApex chartTitle="25 Invoices" :chartHeight="10" :values="values" :months="months" color="#08243D"/>
            </div>
          </div>
          <br>
          <div class="spend">
            <div class="spend-line-graph">
              <p class="tab-title">Monthly Budget Spend</p>
              <BarChartApex :height="250" :values="values" :months="months" color="#4BAD51"/>
              <!-- <line-chart :height="290" :values="values" :dates="dates" :stepSize="stepSize" color="#56caf0"></line-chart> -->
            </div>
            <div class="spend-pie-chart">
              <p class="tab-title">Total Spend</p>
              <DonutChartApex :chartHeight="'160%'" />
            </div>
          </div>
        </div>
        <div class="side">
          <div class="side__item pending-actions">
            <p class="title">Pending Actions</p>
            <ul class="list">
              <li class="list__item"><font-awesome-icon class="icon" icon="circle" />Approve invoice <span class="link">#I001</span></li>
              <li class="list__item"><font-awesome-icon class="icon" icon="circle" />Approve PO <span class="link">#P0012</span></li>
            </ul>
          </div>
          <div class="side__item approval-requests">
            <p class="title">Recent Activity</p>
            <ul class="list">
              <li class="list__item"><font-awesome-icon class="icon" icon="circle" />Invoice created <span class="link">#I001</span></li>
              <li class="list__item"><font-awesome-icon class="icon" icon="circle" />PO created <span class="link">#P001</span></li>
            </ul>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import LineChart from '@/components/charts/budget/LineChart'
import DoughnutChart from '@/components/charts/budget/DoughnutChart'
import AreaLineChartApex from '@/components/charts/apexCharts/AreaLineChart'
import DonutChartApex from '@/components/charts/apexCharts/DoughnutChart'
import BarChartApex from '@/components/charts/apexCharts/BarChart'
export default {
  name: 'home',
  data () {
    return {
      months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      values: [0,	0,	0, 0,	0, 0,	0,	0,	0, 0,],
      stepSize: 2000,
      pieChartData: [0, 0, 0]
    }
  },
  components: {
    LineChart,
    DoughnutChart,
    AreaLineChartApex,
    BarChartApex,
    DonutChartApex
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
      height: 25vh;
      // background-color: $color-white-milk;
      border-radius: $line-height/6;
      // @include shadow;

       @media screen and (min-width: 1600px) {
         height: 20vh;
       }
      
    }

    .unique {
      @include grid_column;
      justify-content: flex-start;
      border: 1px solid $color-white-milk;
      width: 35%;

      .title {
          font-weight: 600;
          font-size: $font-size-small;
          margin-top: $line-height/2;
          margin-bottom: $line-height/2;

          @media screen and (min-width: 1600px) {
            margin-bottom: $line-height*1.5;
          }
        }

      .graph {
        @include grid_row;
        justify-content: center;
      }  

      .chart-labels {
        margin-left: $line-height;
        color: $color-black-medium;

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
      // justify-content: flex-start;
      // align-items: center;
      border: 1px solid $color-white-milk;
      position: relative;
      // background-color: red;
      

      .title {
        font-weight: 600;
        font-size: $font-size-small;
        margin-top: $line-height/1.2;
        position: absolute;
      }

      .pos {
        color: $color-blue-light;
      }

      .desc {
        padding: $line-height/4 0;
        font-weight: 600;
        font-size: $line-height*0.8;
        // color: $color-green-main;
        margin-top: $line-height*1.8;
        position: absolute;
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

  .spend {
    @include grid_row;
  }

  .spend-line-graph {
    width: 65%;
    // background-color: $color-white-milk;
    border-radius: $line-height/6;
    // @include shadow;
    height: 50vh;
    margin: $line-height 2%;
    border: 1px solid $color-white-milk;
    padding: $line-height $line-height/3;
  }

  .spend-pie-chart {
    width: 28%;
    // background-color: $color-white-milk;
    border-radius: $line-height/6;
    // @include shadow;
    height: 50vh;
    margin: $line-height 2%;
    border: 1px solid $color-white-milk;
    padding: $line-height $line-height/3;
  }
}

.side {
  min-height: 90vh;
  border-left: 2px solid $color-gray-light;

  .pending-actions {
    width: 92%;
    height: 30vh;
    margin: 0 4%;
    border-radius: $line-height/3;
    border: 1px solid $color-white-milk;
    background-color: $color-white-milk;
    @include shadow;
  }

  .approval-requests {
    width: 92%;
    height: 40vh;
    margin: $line-height 4%;
    border-radius: $line-height/3;
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

  .pending-actions {
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
</style>
