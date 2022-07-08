import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/index'
import './registerServiceWorker'

// font-awesome
import { library } from '@fortawesome/fontawesome-svg-core'
import { faHome, faClipboardCheck, faShoppingCart, faTruckLoading, faFileInvoice, faBuilding, faPeopleCarry, faHandHoldingUsd, faTasks, faChevronRight, faSearch, faBell, faChevronDown, faUserCircle, faArrowLeft, faSpinner, 
  faTimes, faChevronCircleLeft, faPlusSquare, faCircle, faUsers, faEdit, faFile, faMoneyBill, faDownload, faPlus, faUser, faChartArea, faGift, faPowerOff, faMoneyBillWave, faStar, faCreditCard } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faHome, faClipboardCheck, faShoppingCart, faTruckLoading, faFileInvoice, faBuilding, faPeopleCarry, faHandHoldingUsd, faTasks, faChevronRight, faSearch, faBell, faChevronDown, faUserCircle, faArrowLeft, faSpinner,
  faTimes, faChevronCircleLeft, faPlusSquare, faCircle, faUsers, faEdit, faFile, faMoneyBill, faDownload, faPlus, faUser, faChartArea, faGift, faPowerOff, faMoneyBillWave, faStar, faCreditCard)

Vue.component('font-awesome-icon', FontAwesomeIcon)

// vue table
import {ClientTable} from 'vue-tables-3';
Vue.use(ClientTable);

// Vue axios
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

// Vue form wizard
import VueFormWizard from 'vue-form-wizard'
import 'vue-form-wizard/dist/vue-form-wizard.min.css'
Vue.use(VueFormWizard)

// Vue sweet alert
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';
Vue.use(VueSweetalert2);

// Vue Select
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css';
Vue.component('v-select', vSelect)

// Vue Charts
import VueCharts from 'vue-chartjs'
Vue.use(VueCharts);

//Vue Apex Charts
import VueApexCharts from 'vue-apexcharts'
Vue.use(VueApexCharts)
Vue.component('apexchart', VueApexCharts)

// Vue tab component
import {Tabs, Tab} from 'vue-tabs-component';
Vue.component('tabs', Tabs);
Vue.component('tab', Tab);

// Timeago
import VueTimeago from 'vue-timeago'
Vue.use(VueTimeago, {
  name: 'Timeago', // Component name, `Timeago` by default
  locale: 'en', // Default locale
  // We use `date-fns` under the hood
  // So you can use all locales from it
  locales: {
    'zh-CN': require('date-fns/locale/zh_cn'),
    ja: require('date-fns/locale/ja')
  }
})

//ClickOutside
import vClickOutside from 'v-click-outside'
Vue.use(vClickOutside)

// Overlay
import Loading from 'vue-loading-overlay';
Vue.use(Loading)

// Prevent parent from scrolling
Vue.use(require('vue-prevent-parent-scroll'))

Vue.config.productionTip = false

// Format currency
Vue.filter('toCurrency', function (value, currency) {
  // if (typeof value !== "number") {
  //     return value;
  // }
  var formatter = new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: currency,
      minimumFractionDigits: 2
  });
  return formatter.format(value);
});

// Format Date
import moment from 'moment'
Vue.filter('formatDate', function(value) {
  if (value) {
    return moment(String(value)).format('MM/DD/YYYY hh:mm A')
  }
});

// Format values by rounding off
Vue.filter('round', function (value) {
  if (!value) {
    value = 0
  }

  let decimals = 2

  value = Math.round(value * Math.pow(10, decimals)) / Math.pow(10, decimals)
  return value
})

// Format values to percentage
Vue.filter('percentage', function (value) {
  if (!value) {
    value = 0
  }

  let decimals = 2

  value = Math.round(value * Math.pow(10, decimals)) / Math.pow(10, decimals)
  value = value + '%'
  return value
})

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
