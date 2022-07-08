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
                <div v-if="loading===true" class="loading">
                    <font-awesome-icon class="loading-icon rotating" icon="spinner" />
                    <p class="desc">Setting new password</p>
                </div>
                <form v-if="!loading" class="form" v-on:submit.prevent="setNewPassword()">
                    <p class="desc">New Password</p>
                    <input class="login__form--input" autocomplete="off" type="password" placeholder="Password" v-model="password" required>
                    <p class="desc">Confirm Password</p>
                    <input class="login__form--input" autocomplete="off" type="password" placeholder="Confirm Password" v-model="confirm_password" required>
                    <input class="login__form--submit" type="submit" value="Set Password">
                </form>
                </div>
        </div>
    </div>
</template>

<script>
import auth from '@/services/authentication'
export default {
    name: 'set-password',
    data() {
        return {
            loading: false,
            password: '',
            confirm_password: ''
        }
    },
    computed: {

    },
    methods: {
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

            this.loading = !this.loading
            let payload = {
                "password": this.password,
                "token": this.$route.params.token
            }
            try {
                await auth.setPassword(payload)
                this.$swal({
                    icon: 'success',
                    text: 'Password Reset',
                    showConfirmButton: false,
                });
                this.$router.push('/login');
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

        .loading {
            margin-top: $line-height*2;
            text-align: center;

            .loading-icon {                
                margin: $line-height/3;
                font-weight: bold;
                font-size: $font-size-title;
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
