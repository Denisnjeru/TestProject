<template>
  <div class="home page-container">
    <div class="page">
      <h4 class="page__title">Security</h4>
      <p class="page__desc">Update Password</p>
      <div class="page__content">
        <span v-if="firstTime === true">
          <br>
          <br>
          <div class="page__content--row">
            <p class="element">
                <span class="element__title">Welcome to eProcure. Please reset your password to proceed.</span>
            </p>
          </div>
          <div class="page__content--row" v-if="emailSent === false">
            <p class="element">
                <span class="element__title">Get reset password link on your email - </span>
                <span class="element__content link" @click="requestToken()">Get link</span>
            </p>
          </div>
          <div class="page__content--row" v-else>
            <p class="element">
                <span class="element__title">
                  <strong>Email has been sent, please check your email. </strong>
                  <span class="element__content link" @click="requestToken()"> Resend Email</span>
                </span>
            </p>
          </div>
        </span>
        <div v-else class="form-container">
          <form v-on:submit.prevent="setNewPassword()" class="form">
            <p class="page__content--sub-title">Set new password</p>
            <div class="form-control">
              <label class="label" for="">Password</label>
              <input class="form__input" autocomplete="off" type="password" placeholder="Password" v-model="password" required>
            </div>
            <div class="form-control">
              <label class="label" for="">Confirm Password</label>
              <input class="form__input" autocomplete="off" type="password" placeholder="Confirm Password" v-model="confirm_password" required>
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
import auth from '@/services/authentication'
import { mapGetters } from 'vuex'
export default {
  name: 'home',
  data () {
    return {
      emailSent: false,
      firstTime: false,
      password: '',
      confirm_password: ''
    }
  },
  components: {
    UserActions
  },
  mounted() {
    this.checkFisrtTime()
  },
  computed: {
    ...mapGetters('Auth',['authUser']),
  },
  methods: {
    checkFisrtTime: function() {
        if (this.$route.params.token === 'ft') {
          this.firstTime = true
        }
    },
    async requestToken(){
        let payload = {
            "email": this.authUser.username
        }
        try {
            await auth.resetPassword(payload)
            this.emailSent = true
            this.$swal({
            icon: 'success',
            text: 'Email sent',
            showConfirmButton: false,
            });
        } catch (err) {
            let error = Object.entries(err.response.data)
            this.loading = !this.loading
            this.$swal({
            icon: 'error',
            title: 'Oops...',
            text: error,
            showConfirmButton: false,
            });
        } 
    },
    async setNewPassword(){
        if (this.password !== this.confirm_password) {
            this.password = ''
            this.confirm_password = ''
            this.$swal({
                icon: 'error',
                text: 'Passwords do not match',
                showConfirmButton: false,
            });
            return null

        }

        let payload = {
            "password": this.password,
            "token": this.$route.params.token
        }

        try {
            await auth.setPassword(payload)
            this.$swal({
                icon: 'success',
                text: 'Password Updated. Please login again.',
                showConfirmButton: false,
            });
            this.$store.dispatch('Auth/logout')
            this.$store.dispatch('User/logout')
            this.$router.push('/login')
        } catch (err) {
            let error = Object.entries(err.response.data)
            this.$swal({
            icon: 'error',
            title: 'Oops...',
            text: error,
            showConfirmButton: false,
            });
        } 
    },
  }
}
</script>

<style lang="scss" scoped>

</style>