<template>
  <div id="app" class="wrapper">
    <div class="top-nav" v-if="isAuthenticated">
      <TopNav />
    </div>
    <div class="grid-container">
      <div class="side-nav" v-if="isAuthenticated">
        <SideNav />
      </div>
      <div class="view">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
import TopNav from '@/components/TopNav.vue'
import SideNav from '@/components/SideNav.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'Home',
  data () {
    return {

    }
  },
  created () {
    let route_name = window.location.pathname.split('/')
    if (this.isAuthenticated === false) {     
      if (route_name[1] !== 'set-password') {
        this.$router.push('/login');
      } else {
        this.$router.push('/login');
      }
    } else {
      if (route_name[1] === 'set-password') {
        this.$router.push('/update-password/' + route_name[2]);
        //     :8080/approval/invoice-approval/1/token
      }

      if (this.authUser.gl_structure === false) {
        console.log(this.authUser.gl_structure)
        this.$router.push('/company/setup')
      }
    }
  },
  computed: {
        ...mapGetters('Auth',['isAuthenticated', 'authUser']),
  },
  components: {
    TopNav,
    SideNav
  }
}
</script>

<style lang="scss">
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: $color-black-medium;//#2c3e50;
  font-size: $font-size-small;
}

.wrapper {
  width: 100%;
  height: 100vh;
  background-color: $color-white-pure;
  overflow: hidden;

  .grid-container {
    width: 100%;
    height: 90vh;

    @include grid_row;
    justify-content: flex-start;

    .side-nav {
      width: 20%;
      // width: 5%;
    }

    .view {
      width: 80%;
      // padding: 2%;
      // width: 95%;
    }
  }
}

.page-container {
  @include page-container;
  @include form();

  .wizard-header {
    display: none;
  }
}
</style>
