<template>
    <div class="nav-top">
        <div class="brand">            
            <router-link to="/">
                <img class="brand__logo" src="@/assets/logo.png" alt="logo">
            </router-link>
        </div>
        <div class="shortcuts">
            <div class="left">
                <font-awesome-icon class="back-icon" icon="arrow-left" @click="$router.go(-1)" />
                <input class="search-input" type="text" placeholder="Search...">
                <font-awesome-icon class="search-icon" icon="search" />
            </div>
            <div class="right">
                    <span class="dropdown dropdown-notifications" v-click-outside="onClickOutside" v-on:click="popShowNotifications()">
                        <p>
                            <font-awesome-icon class="notifications__icon" icon="bell" />
                            <sup class="notifications__count">{{ unread_count }}</sup>
                        </p>
                        <!-- <span v-if="showNotifications" class="notications-dropdown__content">
                            test
                        </span> -->
                        <div v-if="showNotifications" class="dropdown-container">
                                <div class="dropdown-toolbar">
                                    <div v-show="hasUnread" class="dropdown-toolbar-actions">
                                    <a href="#" @click.prevent="AllMarkRead()">Mark all as read</a>
                                    </div>

                                    <h3 class="dropdown-toolbar-title">
                                    Notifications ({{ unread_count }})
                                    </h3>
                                </div>
                                <ul class="dropdown-menu">
                                    <notification v-for="notification in notifications"
                                                :key="notification.id"
                                                :notification="notification"
                                                @read="markAsRead(notification)"
                                    />
                                    <li v-if="!hasUnread" class="notification">
                                    You don't have any unread notifications.
                                    </li>
                                    <span class="dropdown-footer-hover">
                                        <div class="dropdown-footer" align="center">
                                            <router-link to="/notifications">View All</router-link>
                                        </div>
                                    </span>
                                </ul>
                        </div>
                    </span>                 
                <div class="user">
                    <p class="user__identity" @click="profile()">
                        <span  v-if="user">
                            <img v-if="user.profile_pic" class="user__identity--pic" :src="user.profile_pic" alt="profile pic">
                            <img v-else class="user__identity--pic" src="@/assets/user.png" alt="profile pic">
                        </span>
                        <img v-else class="user__identity--pic" src="@/assets/user.png" alt="profile pic">
                        <span class="user__name" v-if="authUser">{{authUser.firstname}}</span>
                        <span class="user__name" v-else></span>
                    </p>                   
                    <span v-on:click="popShowMenu()" v-click-outside="onClickOutside2">
                        <font-awesome-icon class="dropdown-dropmenu__icon" icon="chevron-down" />
                        <!-- <div class="dropdown-content"> -->
                        <div class="dropdown-dropmenu" style="width: 180px" v-if="showMenu">
                            <div class="header-nav-current-user">
                                <a class="no-underline user-profile-link px-3 pt-2 pb-2 mb-n2 mt-n1 d-block"> 
                                    Signed in as
                                    <strong class="css-truncate-target" v-if="authUser">{{authUser.firstname}}</strong>
                                    <strong v-else></strong>
                                </a>
                            </div>
                            <div class="dropdown-divider"></div>
                            <span class="dropdown-item dropdown-item-hover" @click="profile()">
                                <font-awesome-icon class="dropdown-content__item--icon" icon="user" />
                                <span class="px-3">Profile</span>
                            </span>
                            <span class="dropdown-item dropdown-item-hover" @click="logout">
                                <font-awesome-icon class="dropdown-content__item--icon" icon="power-off" />
                                <span class="px-3">log out</span>
                            </span>
                        </div>
                    </span>
                </div> 
            </div>               
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import notifications from '@/services/notifications'
import notification from  '@/components/notifications/NotificationDropDown.vue'

export default {
    data() {
        return {
            showNotifications: false,
            unread_count:0,
            notifications: [],
            showMenu: false
        }
    },
    computed: {
        ...mapGetters('Auth',['authUser']),
        ...mapGetters('User',['userType', 'userData']),
        user: function(){
            return this.userData
        },
        hasUnread () {
            return this.unread_count > 0
        }
    },
    mounted(){
        // this.initDropdown()
        this.getunreadcount()
        this.fetchunreadlist()
    },
    components: {
        notification
    },
    methods: {
        popShowNotifications () {
            this.showNotifications = !this.showNotifications
            console.log(this.notifications)
        },
        popShowMenu(){
            this.showMenu = !this.showMenu
            console.log('Menu')
        },
        logout(){
            // let state = this.$store.state;

            // Object.keys(state).forEach(key => {
            //     if (key != 'Auth') {
            //         state[key] = null
            //     } 
            // }); @click="logout()"
            
            this.$store.dispatch('Auth/logout')
            this.$store.dispatch('User/logout')
            this.$router.push('/login')
        },
        profile() {
            if (this.userType == 'supplier') {
                this.$router.push('/supplier/home/profile');
            } else {
                this.$router.push('/profile/' + this.authUser.user_id);
            }
        },
        async getunreadcount(){
            try{
                const response = await notifications.unread_notifications_count()
                this.unread_count = response.data.unread_count
            } catch(error){
                console.log(error)
            }
        },
        async fetchunreadlist(){
            try{
                const response = await notifications.unread_notifications_list()
                console.log(response.data.unread_list)
                this.notifications = response.data.unread_list
            }catch(error){
                console.log(error)
            }
        },
        async AllMarkRead(){
            try{
                await notifications.mark_all_as_read()
                this.showNotifications = !this.showNotifications
                this.getunreadcount()
            }catch(error){
                console.log(error)
            }
        },
        onClickOutside () {
            this.showNotifications = false
        },
        onClickOutside2(){
            this.showMenu =false
        }
    },
}
</script>

<style lang="scss" scoped>
.d-block {
    display: block !important;
}
.no-underline {
    text-decoration: none !important;
}
.px-3 {
    padding-right: 16px !important;
    padding-left: 16px !important;
}
.pb-2 {
    padding-bottom: 8px !important;
}
.pt-2 {
    padding-top: 8px !important;
}
.mb-n2 {
    margin-bottom: -8px !important;
}
.mt-n1 {
    margin-top: -4px !important;
}
.nav-top {
    width: 100%;
    height: 9vh;
    @include grid_row;
    z-index: 10;
    @include bottom-shadow;

    .brand {
        // background-color: $color-white-pure;
        width: 18.6%;
        position: relative;
        padding: $line-height/2;
        // @include shadow;
        // margin-top: 12vh;
        @include grid_row;
        //responsive
        // display: none;

        &__logo {
            height: $line-height*0.9;
            margin-left: $line-height/3;
        }
        
    }

    .shortcuts {
        width: 100%;
        @include grid_row;
        .left {
            width: 15%;
            margin-left: 2%;
            @include grid_row;

            .back-icon {
                margin-right: $line-height;
                font-size: $font-size-title;
                color: $color-green-main;
                cursor: pointer;
            }

            .search-input {
                padding: $line-height/3 $line-height;
                border-radius: $line-height/4;
                border: none;
                background-color: $color-white-milk;
                @include shadow();

                &:focus {
                outline: none;
                }
            }

            .search-icon {
                margin-left: -$line-height;
            }
        }

        .right {
            @include grid_row;
            justify-content: flex-end;
            padding: 0 $line-height;
// here
            .dropdown-container{
                cursor: pointer;
                position: relative;
                display: inline-block;
            }
            
            .dropdown-toolbar {
                padding-top: 6px;
                padding-left: 20px;
                padding-right: 20px;
                padding-bottom: 5px;
                background-color: #fff;
                border-bottom: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 4px 4px 0 0;
            }
            .dropdown-toolbar .dropdown-toolbar-actions {
                float: right;
            }
            .dropdown-toolbar .dropdown-toolbar-title {
                margin: 0;
                font-size: 14px;
            }
            .dropdown-notifications .dropdown-toolbar{
                padding: 9.6px 12px;
            }
            .dropdown-notifications .dropdown-footer {
                padding: 1.6px 12px;
            }
            .dropdown-notifications .dropdown-toolbar {
                background: #fff;
            }
            .dropdown-notifications .dropdown-footer {
                background: #eeeeee;
                padding: 9.6px 20px;
            }
            .dropdown-container > .dropdown-menu {
                position: static;
                z-index: 1000;
                float: none!important;
                padding: 10px 0;
                margin: 0;
                border: 0;
                background: transparent;
                border-radius: 0;
                -webkit-box-shadow: none;
                box-shadow: none;
                max-height: 330px;
                overflow-y: auto;
            }
            .dropdown-container > .dropdown-menu + .dropdown-menu {
                padding-top: 0;
            }
            .dropdown-menu > li > a {
                overflow: hidden;
                white-space: nowrap;
                word-wrap: normal;
                text-decoration: none;
                text-overflow: ellipsis;
                -o-text-overflow: ellipsis;
                -webkit-transition: none;
                -o-transition: none;
                transition: none;
            }
            .dropdown-menu .notification{
                padding: 9.6px 12px;
            }
            .dropdown-notifications > .dropdown-container,
            .dropdown-notifications > .dropdown-menu {
                width: 450px;
                max-width: 450px;
            }
            .dropdown-notifications .dropdown-menu {
                padding: 0;
            }
            .notificationstv {
                list-style: none;
                padding: 0;
            }
            .dropdown-footer {
                padding: 2.5px 20px;
                border-top: 1px solid #ccc;
                // border-top: 1px solid rgba(0, 0, 0, 0.15);
                border-radius: 0 0 4px 4px;
            }
            .dropdown-footer-hover{
                & :hover{
                    background: #ccc;
                }
            }

            .dropdown-notifications {
                cursor: pointer;
                .dropdown-container {
                    display: block;
                    position: absolute;
                    background-color: #fff;
                    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                    z-index: 20;
                    margin-top: 4.2vh;
                    margin-left: -20ch;
                    width: 40ch;
                    padding: $line-height/2;
                }
            
                .notification-icon.hide-count:after {
                    display: none;
                }
            
                .dropdown-toolbar .dropdown-toolbar-actions {
                    margin-top: -2px;
                    font-size: 13px;
                }
            
                .notification-mark-read {
                    float: right;
                    float: right;
                    color: #333;
                    opacity: 0.4;
                
                    &:hover {
                        opacity: .8;
                    }
                }
            
                .notification-action {
                    margin-top: 5px;
                    margin-bottom: 2px;
                }
            
                .notification .media-body {
                    padding-top: 0px;
                }
            
                .media-object img {
                    width: 64px;
                }
            }
// there
            .notications-dropdown {
                cursor: pointer;
                position: relative;
                display: inline-block;

                &__content {
                    display: block;
                    position: absolute;
                    background-color: #f1f1f1;
                    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                    z-index: 20;
                    margin-top: 4.2vh;
                    margin-left: -20ch;
                    width: 44ch;
                    padding: $line-height/2;
                }
            }

            .notications-dropdown {
                cursor: pointer;
                position: relative;
                display: inline-block;

                &__content {
                    display: block;
                    position: absolute;
                    background-color: #f1f1f1;
                    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                    z-index: 20;
                    margin-top: 4.2vh;
                    margin-left: -20ch;
                    width: 44ch;
                    padding: $line-height/2;
                }
            }

            .notifications {
                display: block;
                margin-right: $line-height/2;
                &__icon {
                    color: $color-blue-main;
                    font-size: $font-size-title;
                }

                &__count {
                    color: $color-blue-light;
                    font-weight: 600;
                    margin-top: -$line-height;
                }
            }

            .user {
                @include grid_row;
                &__identity {
                    @include grid_row;
                    margin: 0 $line-height/4;                    

                    &--pic {
                        height: $line-height*1.5;
                        width: $line-height*1.5;
                        margin: 0 $line-height/4;
                        border-radius: 50%;
                        border: 2px solid $color-blue-main;
                        cursor: pointer;

                        &:hover {
                           border: 2px solid $color-blue-light; 
                        }
                    }
                }

                &__icon {
                    font-size: $line-height*1.5;
                    margin: $line-height/3;                    
                }

                .dropdown-dropmenu{
                    position: absolute;
                    width: 160px;
                    list-style: none;
                    background-clip: padding-box;
                    border: 1px solid #fff;
                    border-radius: 6px;  
                    display: block;
                    background-color: #fff;
                    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                    z-index: 20;
                    margin-top: 4.2vh;
                    margin-left: -20ch;
                    width: 40ch;
                    padding: $line-height/2;
                    
                    &__icon {
                        color: $color-green-main;
                        cursor: pointer;
                    }

                    .header-nav-current-user{
                        padding:0;
                        font-size: inherit;

                        .user-profile-link {
                            color: #031b4e;
                        }

                        .css-truncate-target{
                            max-width: 100%;
                        }
                    }

                    .dropdown-divider{
                        display: block;
                        height: 0;
                        margin:8px 0;
                        border-top: 1px solid #031b4e;
                    }

                    .dropdown-item {
                        cursor: pointer;
                        display: block;
                        padding: 4px 8px 10px 16px;
                        overflow: hidden;
                        // color: #8b949e;
                        text-overflow: ellipsis;
                        white-space: nowrap;

                        &:hover {
                        //    border: 2px solid $color-blue-light; 
                            background: #F3F5F9;
                        }
                    }

                }
                .dropdown-dropmenu-sw{
                    right:0;
                    left: auto;
                }
            }

            .dropdown {
                &__icon {
                    color: $color-green-main;
                    cursor: pointer;
                }
            }

            
        }
    }
}
</style>