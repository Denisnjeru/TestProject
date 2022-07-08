<template>
    <div class="login-new">
        <div class="top">
            <div class="content">
                <div class="top__nav">
                    <div class="brand">
                        <img src="@/assets/logo.png" alt="eProcure" class="brand__logo">
                    </div>
                    <ul class="top__nav--list">
                        <li class="item">Features</li>
                        <li class="item">Pricing</li>
                        <li class="item">Help</li>
                        <li class="item">Contact</li>
                    </ul>
                </div>
                <div class="desc">
                    <!-- <p class="desc__heading">Lorem ipsum dolor sit amet consectetur adipisicing elit. </p> -->
                </div>
            </div>
        </div>
        <div class="bottom">
            <div class="details">

            </div>
            <div class="login-form">
                <div class="login-form__form">

                </div>
                <p class="register">Request for account <a href="" class="register__link">Contact us</a></p>
            </div>
        </div>
        <div class="shortcuts">
            <div class="border"></div>
            <div class="details">
                <p class="copyright">©eProcure</p>
                <ul class="links">
                    <li class="link">Privacy</li>
                    <li class="link">Terms & Conditions</li>
                    <li class="link">Help</li>
                    <li class="link">Contact</li>
                </ul>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.login-new {
    width: 119%;
    height: 110vh;
    background-color: $color-white-pure;
}

.top {
    height: 50vh;
    width: 100%;
    background-color: $color-blue-main;
    padding: 0 5%;

    .content {
        top: 0;
        position: fixed;
        width: 100%;
    }

    &__nav {
        width: 100%;
        padding: $line-height 0;
        color: $color-gray-light;
        display: flex;
        flex-flow: row nowrap;

        .brand {
            
            &__logo {
                height: $line-height*2;
            }
        }

        &--list {
            display: flex;
            flex-flow: row nowrap;
            align-self: center;
            padding-left: $line-height*3;

            .item {
                padding: 0 $line-height/2;
            }
        }
    }

    .desc {
        &__heading {
            font-size: $line-height;
            font-weight: 600;
            width: 35%;
            color: $color-gray-light;
        }
    }
}

.bottom {
    width: 100%;
    height: 50vh;
    background-color: $color-white-pure;
    padding: $line-height 10%;

    display: flex;
    flex-flow: row nowrap;

    .details {
       width: 65%; 
       height: 100%;
    }

    .login-form {
        width: 35%;
        height: 100%;
        display: flex;
        flex-flow: column nowrap;

        &__form {
            height: 75vh;
            width: 100%;
            background-color: $color-white-milk;
            margin-top: -40vh;
            border-radius: $line-height/3;
            align-self: flex-end;
            @include shadow();
        }

        .register {
            align-self: center;
            padding: $line-height/2 0;
            color: $color-black-main;
            font-size: 14px;

            &__link {
                color: $color-blue-light;
                font-weight: 600;
                padding: 0 $line-height/4;
            }
        }
    }
}

.shortcuts {
    height: 10vh;
    width: 100%;
    background-color: $color-white-pure;
    padding: 0 10%;
    

    .border {
        background-color: $color-blue-medium;
        width: 100%;
        height: 2px;
    }

    .details {
        display: flex;
        flex-flow: row nowrap;
        padding: $line-height 0;

        .copyright {
            color: $color-black-main;
        }

        .links {
            padding-left: $line-height*3;
            display: flex;
            flex-flow: row nowrap;

            .link {
                padding: 0 $line-height/2;
                color: $color-gray-dark;
                font-size: 14px;
            }
        }
    }
}
</style>