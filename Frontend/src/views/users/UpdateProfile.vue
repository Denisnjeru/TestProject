<template>
  <div class="home page-container">
    <div class="page">
      <h4 class="page__title">User Profile</h4>
      <p class="page__desc">Update</p>
      <div class="page__content">

        <br>
        <div class="tab-shortcuts">
            <span class="tab-shortcuts__item" v-if="profile.user.username === authUser.username" @click="updatePassword()">Update Password</span>
        </div>
        <div class="form-container">
          <form action="" class="form">
            <p class="page__content--sub-title">Personal Information</p>
            <div class="page__content--row row-2">
              <p class="element">
                  <span class="element__title">First Name: </span>
                  <span class="element__content">{{profile.user.first_name}}</span>
              </p>
              <p class="element">
                  <span class="element__title">Last Name: </span>
                  <span class="element__content">{{profile.user.last_name}}</span>
              </p>
            </div>
            <div class="page__content--row row-2">
              <p class="element">
                  <span class="element__title">Job Role: </span>
                  <span class="element__content">{{profile.company_user.company_role.name}}</span>
              </p>
              <p class="element">
                  <span class="element__title">Department: </span>
                  <span class="element__content">{{profile.company_user.department.department_name}}</span>
              </p>
            </div>

            <p class="page__content--sub-title">Contact Information</p>
            <div class="page__content--row">
              <p class="element">
                  <span class="element__title">Email: </span>
                  <span class="element__content">{{profile.user.email}}</span>
              </p>
            </div>
            <div class="form-control">
              <label class="label" for="">Phone</label>
              <input type="text" class="form__input" v-model="profile.phone_no">
            </div>
            <div class="form-control">
              <input type="submit" class="form__submit">
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="page-side">
      <UserActions /> 
    </div>
  </div>
</template>

<script>
import UserActions from '@/components/actions/User.vue'
import user from '@/services/user'
import auth from '@/services/authentication'
import { mapGetters } from 'vuex'
export default {
  name: 'home',
  data () {
    return {
      profile: null
    }
  },
  components: {
    UserActions
  },
  created() {
    this.getProfile()
  },
  computed: {
    ...mapGetters('Auth',['authUser']),
  },
  methods: {
    async getProfile() {
      try {
        const response = await user.userProfile(this.$route.params.id)
        this.profile = response.data
      } catch (err) {
        console.log(err)
      }
    },
    async updatePassword() {
      let payload = {
        "email": this.profile.user.username
      }
      try {
          await auth.resetPassword(payload)
          this.$swal({
          icon: 'success',
          text: 'Reset password email has been sent to your email.',
          showConfirmButton: false,
          });
      } catch (err) {
          let error = Object.entries(err.response.data)
          this.$swal({
          icon: 'error',
          title: 'Oops...',
          text: error,
          showConfirmButton: false,
          });
      }
    }
  }
}
</script>

<style lang="scss" scoped>

</style>