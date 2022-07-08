<template>
  <div class="nav">
    <div class="brand">
        <router-link to="/">
        <img class="brand__logo" src="@/assets/logo.png" alt="logo">
        </router-link>
    </div>
    <div class="list">
        <div class="list__item">
            <p class="list__item--desc active">
                <router-link to="/">
                    <span class="desc">                      
                        <font-awesome-icon class="main-icon" icon="home" />
                        <span class="name">Dashboard</span> 
                    </span>
                </router-link>
            </p>
        </div>
        <p class="list__title">Modules</p>
        <div class="list__item">
            <p class="list__item--desc">
                <router-link to="/4">
                    <span class="desc">  
                        <font-awesome-icon class="main-icon" icon="clipboard-check" />
                        <span class="name">Requisition</span>
                    </span>
                </router-link>
            </p>
        </div>
        <div class="list__item">
            <p class="list__item--desc">
                <router-link to="/2">
                    <span class="desc">
                        <font-awesome-icon class="main-icon" icon="shopping-cart" />
                        <span class="name">Purchase Order</span>
                    </span>
                </router-link>
            </p>
        </div>
        <div class="list__item">
            <p class="list__item--desc">
                <router-link to="/1">
                    <span class="desc">
                        <font-awesome-icon class="main-icon" icon="truck-loading" />
                        <span class="name">Receive Goods</span>
                    </span>
                </router-link>
            </p>
        </div>
        <div class="list__item">
            <p class="list__item--desc">
                <router-link to="/2">
                    <span class="desc">
                        <font-awesome-icon class="main-icon" icon="file-invoice" />
                        <span class="name">Invoice</span>
                    </span>
                </router-link>
            </p>
        </div>
        <p class="list__title">Settings</p>
        <div class="list__item dropdown">
            <p class="list__item--desc">
                <span class="desc">
                    <font-awesome-icon class="main-icon" icon="building" />
                    <span class="name">Company</span>
                </span>
                <font-awesome-icon class="dropdown-icon" icon="chevron-right" />
            </p>
            <div class="list__item--dropdown dropdown-content">
            <p class="dropdown-content__item">
                <router-link to="/customers/all">Company Management</router-link>
            </p>
            <p class="dropdown-content__item">
                <router-link to="/customers/all">User Management</router-link>
            </p>
            </div>
        </div>
        <div class="list__item dropdown">
            <p class="list__item--desc">
                <span class="desc">
                    <font-awesome-icon class="main-icon" icon="people-carry" />
                    <span class="name">Supplers & Items</span>
                </span>
                <font-awesome-icon class="dropdown-icon" icon="chevron-right" />
            </p>
            <div class="list__item--dropdown dropdown-content">
                <p class="dropdown-content__item">
                    <router-link to="/vendors/all">Supplier Management</router-link>
                </p>
                <p class="dropdown-content__item">
                    <router-link to="/vendors/verified">Items Management</router-link>
                </p>
            </div>
        </div>
        <div class="list__item dropdown">
            <p class="list__item--desc">
                <span class="desc">
                    <font-awesome-icon class="main-icon" icon="hand-holding-usd" />
                    <span class="name">Accounts</span>
                </span>
                <font-awesome-icon class="dropdown-icon" icon="chevron-right" />
            </p>
            <div class="list__item--dropdown dropdown-content">
                <p class="dropdown-content__item">
                    <router-link to="/vendors/verified">GL Accounts</router-link>
                </p>
                <p class="dropdown-content__item">
                    <router-link to="/vendors/verified">Tax Management</router-link>
                </p>
                <p class="dropdown-content__item">
                    <router-link to="/vendors/verified">Budget Management</router-link>
                </p>
                <p class="dropdown-content__item">
                    <router-link to="/vendors/verified">Shipping</router-link>
                </p>
            </div>
        </div>
        <div class="list__item dropdown">
            <p class="list__item--desc">
                <span class="desc">
                    <font-awesome-icon class="main-icon" icon="hand-holding-usd" />
                    <span class="name">Workflow</span>
                </span>
                <font-awesome-icon class="dropdown-icon" icon="chevron-right" />
            </p>
            <div class="list__item--dropdown dropdown-content">
            <p class="dropdown-content__item">
                <router-link to="/shops/all">Roles</router-link>
            </p>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Nav',
  components: {
    
  }
}
</script>

<style lang="scss" scoped>
.nav {
    height: 100vh;
    width: 100%;
    background-color: $color-blue-main;  
    overflow: hidden;
    @include shadow;
}

.brand {
    width: 100%;
    background-color: $color-white-pure;
    padding: $line-height/3;
    margin-top: 5vh;

    @media screen and (max-width: 1440px) {
        margin-bottom: $line-height/2;
    }

    @media screen and (max-width: 1024px) {
        padding-right: $line-height/4;
    }

    &__logo {
        height: $line-height*2;
        background-color: $color-white-pure;

        @media screen and (max-width: 1024px) {
            height: $line-height*1.5;
            width: $line-height*1.5;
            margin-right: $line-height/4;
        }
    }
}

.list {
    height: 88vh;    
    padding: $line-height/2 0;

    &__title {
        text-transform: uppercase;
        font-weight: 900;
        color: $color-gray-medium;
        font-size: $line-height/2;
        padding-top: $line-height/2;
        padding-bottom: $line-height/4;
    }

    .dropdown {
      @include drop-down();
      display: block;

      .list__item--desc {
          @include grid_row;
      }

      &:hover {
          .dropdown-icon {
            transform: rotate(90deg);
            transition: all .35s ease-in-out;
        }
      }

      .dropdown-content { 
          position: relative;
          background-color: transparent;
          box-shadow: none;
          color: $color-gray-medium;

          &__item {
            margin: $line-height/2 0;
            cursor: pointer;

            &:hover {
                color: $color-blue-medium;    
                opacity: 1.0;            
            }
          }
      }
    }

    &__item {
        color: $color-white-pure;
        
        &:first-child {
            margin-top: 0;
        }
        &:last-child {
            margin-bottom: 0;
        }

        &--desc {
            @include grid_row;
            justify-content: space-between;
            cursor: pointer;

            .desc {
                @include grid_row;

                .main-icon {
                    margin-right: $line-height/8;
                    width: $line-height;
                }
            }

            &:hover {
                color: $color-blue-medium;
            }
            

            .superscript {
                color: $color-green-main;
            }
        }

        .router-link-exact-active {
            color: $color-blue-light;
            font-weight: 600;
        }
    }
}
</style>