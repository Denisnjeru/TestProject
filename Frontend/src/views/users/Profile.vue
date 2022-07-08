<template>
  <div class="home page-container">
    <div class="page">
      <h4 class="page__title">User Profile</h4>
      <p class="page__desc">View user profile</p>
      <div class="page__content">    
        <span v-if="profile">
        <br>
        <div class="tab-shortcuts" v-if="profile.user.username === authUser.username">
            <span class="tab-shortcuts__item" @click="updatePassword()">Update Password</span>
        </div>

        <img v-if="profile.profile_pic" class="profile-pic" :src="profile.profile_pic" alt="profile pic">
        <img v-else class="profile-pic" src="@/assets/user.png" alt="profile pic">
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
        <p class="page__content--sub-title">Contact Information</p>
        <div class="page__content--row">
            <p class="element">
                <span class="element__title">Phone: </span>
                <span class="element__content">{{profile.phone_no}}</span>
            </p>
        </div>
        <div class="page__content--row">
            <p class="element">
                <span class="element__title">Email: </span>
                <span class="element__content">{{profile.user.username}}</span>
            </p>
        </div>
        <p class="page__content--sub-title">Privileges</p>
        <div class="page__content--row">
            <p class="element">
                <span class="element__title">Role: </span>
                <span class="element__content">{{profile.company_user.company_role.name}}</span>
            </p>
        </div>
        <p class="page__content--sub-title">Activity</p>
        <div class="page__content--row row-2">
            <p class="element">
                <span class="element__title">Created: </span>
                <span class="element__content">{{profile.company_user.user.date_joined  | formatDate}}</span>
            </p>
            <p class="element">
                <span class="element__title">Last Login: </span>
                <span class="element__content">{{profile.company_user.user.last_login  | formatDate}}</span>
            </p>
        </div>
        <div class="page__content--row buttons">
            <router-link :to="'/profile/update/' + profileId">
              <button class="buttons__button">Update</button>
            </router-link>
            <!-- <button class="buttons__button delete">Delete</button> -->
        </div>
        </span> 
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
import { mapGetters } from 'vuex'
export default {
  name: 'home',
  data () {
    return {
      profile: null,
      profileId: null
    }
  },
  components: {
    UserActions
  },
  mounted() {
    this.getProfile()
  },
  computed: {
      ...mapGetters('Auth',['authUser']),
  },
  methods: {
    async getProfile() {
      try {
          this.profileId = this.$route.params.id
        const response = await user.userProfile(this.$route.params.id)
        this.profile = response.data
        console.log(this.profile)
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
.profile-pic {
    height: $line-height*2.5;
    width: $line-height*2.5;
    margin: 0 $line-height/4;
    border-radius: 50%;
    border: 2px solid $color-blue-main;
    margin-top: $line-height;
}
</style>