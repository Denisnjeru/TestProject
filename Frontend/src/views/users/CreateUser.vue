<template>
  <div class="home page-container">
    <div class="page">
      <h4 class="page__title">Company User</h4>
      <p class="page__desc">Create user</p>
      <div class="page__content">
        <div class="form-container">
          <form class="form" v-on:submit.prevent="CreateUser()">
            <p class="page__content--sub-title">Personal Information</p>
            <div class="form-control">
              <label class="label" for="">First Name</label>
              <span class="error-message" ref="first_name-error"></span>
              <input type="text" ref="first_name" class="form__input" required v-model="user.first_name">
            </div>
            <div class="form-control">
              <label class="label" for="">Last Name</label>
              <span class="error-message" ref="last_name-error"></span>
              <input type="text" ref="last_name" class="form__input" required v-model="user.last_name">
            </div>
            <div class="form-control">
              <label class="label" for="">Email</label>
              <span class="error-message" ref="email-error"></span>
              <input type="email" ref="email" class="form__input" required v-model="user.email">
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
export default {
  name: 'home',
  data () {
    return {
      payload: {},
      user:  {},
    }
  },
  components: {
    UserActions
  },
  mounted() {
    this.payload = {
      user: this.user,
    }
  },
  computed: {

  },
  methods: {
    async CreateUser() {
      try {
        const response = await user.createUser(this.payload)
        this.$router.push('/users/');
      } catch (err) {
        let error = Object.entries(err.response.data)
        console.log(error)
      }
    },
  }
}
</script>

<style lang="scss" scoped>

</style>
