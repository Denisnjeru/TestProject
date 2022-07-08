<template>
    <div class="login">
        <div class="container">
            <div class="illustration">
                <div class="logo">
                    <!-- <img class="login__form--logo" src="@/assets/logo.png" alt="logo"> -->
                </div>
                <div class="illustration__img">
                    <img class="" src="@/assets/login.svg" alt="logo">
                </div>
            </div>

            <div class="login__form">
                <img class="login__form--logo" src="@/assets/logo.png" alt="logo">
                <p class="login__form--title">Welcome Back</p>
                <p class="login__form--desc">Promoting good governance,transparency and integrity in the procurement process</p>
                <!-- <p class="login__form--sub-title">Login</p> -->
                <div v-if="loading" class="loading">
                    <font-awesome-icon class="loading-icon" icon="spinner" />
                    <p class="desc">logging in ...</p>
                </div>
                <form v-if="!loading" class="form" v-on:submit.prevent="login()">
                    <p class="error">{{authError}}</p>
                    <input class="login__form--input" type="email" placeholder="Email" v-model="username" required>
                    <input class="login__form--input" autocomplete="off" type="password" placeholder="Password" v-model="password" required>
                    <input class="login__form--submit" type="submit" value="Login">
                </form>
                <router-link to="/reset-password">
                    <p class="reset_password">Forgot password?</p>
                </router-link>
                </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Cookies from 'js-cookie'

export default {
    name: 'login',
    data() {
        return {
            username: '',
            password: '',
            previousRoute: '',
            loading: false,
        }
    },
    computed: {
        ...mapGetters('Auth',['authUser', 'authStatus', 'authError']),
    },
    methods: {
        async login(){
            this.loading = !this.loading
            const { username, password } = this
            this.$store.dispatch('Auth/login', {  username, password })
            .then(() => {
                if(this.authStatus === 2) {
                    this.$store.dispatch('User/getUser')
                    .then(() => {

                    })

                    const accessToken = Cookies.get('token')
                    if (this.authUser.last_login.length === 0) {
                        console.log(this.authUser.last_login.length)
                        this.$router.push('/update-password/ft');
                        return false
                    }
                    if (this.authUser.gl_structure === false) {
                        this.$router.push('/company/setup');
                    }
                    this.$router.push('/');
                } else if (this.authStatus === 3) {
                    this.loading = !this.loading
                } else {
                    this.loading = !this.loading
                }
            })
        },
    },
    beforeRouteEnter(to, from, next) {
        next(vm => {
            vm.previousRoute = from
        });
    },

}
</script>

<style lang="scss" scoped>
.login {
    width: 119%;
    height: 110vh;
    background-color: $color-white-milk;
    @include grid_row;
    justify-content: center;
    padding: 20vh 0;
    padding-top: 30vh;

    .container {
        background-color: $color-white-pure;
        width: 70%;
        height: 80vh;
        border-radius: $line-height/4;
        @include shadow;
        @include grid_row;

        .illustration {
            width: 60%;
            height: 100%;
            // background-color: $color-white-milk;
            padding: $line-height;
        }

        .logo {
            width: 100%;
            @include grid_row;
            // justify-content: center;
            padding-bottom: $line-height;
            height: $line-height;
        }

        .reset_password {
            margin-top: $line-height;
            color: $color-gray-dark;
            cursor: pointer;

            &:hover {
                color: $color-green-main;
            }
        }

        .login__form {
            width: 45%;
            height: 100%;
            padding: $line-height;
            background-color: $color-white-milk;
            // background-image: url("../../assets/login.svg");
            // background-repeat: no-repeat;
            // background-attachment: fixed;
            // background-position: center;
            padding-top: $line-height*1.5;

            &--logo {
                height: $line-height*1.5;
            }

            &--title {
                font-size: $line-height*1.2;
                margin: $line-height/2 0;
                font-weight: 900;
            }

            &--desc {
                color: $color-gray-dark;
                // font-size: $font-size-text;
            }

            .form {
                padding: $line-height/3 0;
                @include grid_column;
                align-items: flex-start;
                margin-top: $line-height;
            }

            &--sub-title {
                margin-top: $line-height*1.5;
                font-size: $font-size-title;
                color: $color-blue-light;
                font-weight: 600;
            }

            &--input {
                margin: $line-height/2 0;
                border: none;
                padding: $line-height/2 $line-height/4;
                background-color: $color-white-pure;
                width: 100%;
                border-bottom: 2px solid $color-gray-light;

                &:focus {
                    outline: none;
                }
            }

            &--submit {
                margin-top: $line-height/2;
                border: none;
                padding: $line-height/2 $line-height;
                background-color: $color-blue-main;
                color: $color-white-milk;
                font-weight: 600;
                border-radius: $line-height/4;
                cursor: pointer;
            }
        }
    }
}
</style>
