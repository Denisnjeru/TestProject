<template>
    <div class="nav-side">
        <div class="list">
            <p class="list__collapse">
                <font-awesome-icon icon="chevron-circle-left" />
            </p>
            <div class="list__item">
                <p class="list__item--desc active">
                    <router-link to="/" v-if="userType === 'client'">
                        <span class="desc">
                            <font-awesome-icon class="main-icon" icon="home" />
                            <span class="name">Dashboard</span>
                        </span>
                    </router-link>
                    <router-link to="/supplier" v-if="userType === 'supplier'">
                        <span class="desc">
                            <font-awesome-icon class="main-icon" icon="home" />
                            <span class="name">Dashboard</span>
                        </span>
                    </router-link>
                </p>
            </div>
            <p class="list__title">Modules</p>
            <span v-if="userType === 'supplier'">
                <div class="list__item">
                    <p class="list__item--desc">
                        <router-link to="/supplier/home/purchase-orders">
                            <span class="desc">
                                <font-awesome-icon class="main-icon" icon="shopping-cart" />
                                <span class="name">Purchase Order</span>
                            </span>
                        </router-link>
                    </p>
                </div>
                <div class="list__item">
                    <p class="list__item--desc">
                        <router-link to="/supplier/home/issued-items">
                            <span class="desc">
                                <font-awesome-icon class="main-icon" icon="truck-loading" />
                                <span class="name">Issue Goods</span>
                            </span>
                        </router-link>
                    </p>
                </div>
                <div class="list__item">
                    <p class="list__item--desc">
                        <router-link to="/supplier/home/invoices">
                            <span class="desc">
                                <font-awesome-icon class="main-icon" icon="file-invoice" />
                                <span class="name">Invoice</span>
                            </span>
                        </router-link>
                    </p>
                </div>
                <div class="list__item">
                    <p class="list__item--desc">
                        <router-link to="/supplier/home/items">
                            <span class="desc">
                                <img class="main-icon img" src="@/assets/inventory.png" alt="I">
                                <span class="name">Catalogue</span>
                            </span>
                        </router-link>
                    </p>
                </div>
                <div class="list__item">
                    <p class="list__item--desc">
                        <router-link to="/supplier/home/reports">
                            <span class="desc">
                                <img class="main-icon img" src="@/assets/reports.png" alt="R">
                                <span class="name">Reports</span>
                            </span>
                        </router-link>
                    </p>
                </div>
            </span>
            <span v-if="userType === 'client'">
                <div class="list__item">
                    <p class="list__item--desc">
                        <router-link to="/requisitions">
                            <span class="desc">
                                <font-awesome-icon class="main-icon" icon="clipboard-check" />
                                <span class="name">Requisition</span>
                            </span>
                        </router-link>
                    </p>
                </div>
                <!-- <div class="list__item">
                    <p class="list__item--desc">
                        <router-link to="/vouchers">
                            <span class="desc">
                                <font-awesome-icon class="main-icon" icon="gift" />
                                <span class="name">Voucher</span>
                            </span>
                        </router-link>
                    </p>
                </div> -->
                <div class="list__item">
                    <p class="list__item--desc">
                        <router-link to="/purchase-orders">
                            <span class="desc">
                                <font-awesome-icon class="main-icon" icon="shopping-cart" />
                                <span class="name">Purchase Order</span>
                            </span>
                        </router-link>
                    </p>
                </div>
                <div class="list__item">
                    <p class="list__item--desc">
                        <router-link to="/receive-goods">
                            <span class="desc">
                                <font-awesome-icon class="main-icon" icon="truck-loading" />
                                <span class="name">Receive Goods</span>
                            </span>
                        </router-link>
                    </p>
                </div>
                <div class="list__item">
                    <p class="list__item--desc">
                        <router-link to="/invoices">
                            <span class="desc">
                                <font-awesome-icon class="main-icon" icon="file-invoice" />
                                <span class="name">Invoice</span>
                            </span>
                        </router-link>
                    </p>
                </div>
                <div class="list__item">
                    <p class="list__item--desc">
                        <router-link to="/budget" v-if="budgetModuleStatus === 'active'">
                            <span class="desc">
                                <font-awesome-icon class="main-icon" icon="money-bill" />
                                <span class="name">Budgeting</span>
                            </span>
                        </router-link>
                    </p>
                </div>
                <!-- <div class="list__item">
                    <p class="list__item--desc">
                        <router-link to="/5">
                            <span class="desc">
                                <img class="main-icon img" src="@/assets/inventory.png" alt="I">
                                <span class="name">Inventory</span>
                            </span>
                        </router-link>
                    </p>
                </div> -->

            <div class="list__item">
                <p class="list__item--desc">
                    <router-link to="/spend-management">
                        <span class="desc">
                            <img class="main-icon img" src="@/assets/inventory.png" alt="I">
                            <span class="name">Spend Management</span>
                        </span>
                    </router-link>
                </p>
            </div>

            <div class="list__item dropdown">
                <p class="list__item--desc">
                    <span class="desc">
                        <font-awesome-icon class="main-icon" icon="people-carry" />
                        <span class="name">Supplier Management</span>
                    </span>
                    <font-awesome-icon class="dropdown-icon" icon="chevron-right" />
                </p>
                <div class="list__item--dropdown dropdown-content">
                    <p class="dropdown-content__item">
                        <router-link to="/suppliers">Supplier Catalogue</router-link>
                    </p>
                    <p class="dropdown-content__item">
                        <router-link to="/items">Items Management</router-link>
                    </p>
                    <p class="dropdown-content__item">
                        <router-link to="/items-capping">Items Capping</router-link>
                    </p>
                    <p class="dropdown-content__item">
                        <router-link to="/categories">Category Management</router-link>
                    </p>
                    <p class="dropdown-content__item">
                        <router-link to="/uoms">UOM Management</router-link>
                    </p>
                    <p class="dropdown-content__item">
                        <router-link to="/payment-terms">Payment Terms Management</router-link>
                    </p>
                </div>
            </div>            

            <div class="list__item dropdown">
                <p class="list__item--desc">
                    <span class="desc">
                        <font-awesome-icon class="main-icon" icon="chart-area" />
                        <span class="name">Supplier Performance</span>
                    </span>
                    <font-awesome-icon class="dropdown-icon" icon="chevron-right" />
                </p>
                <div class="list__item--dropdown dropdown-content">
                    <p class="dropdown-content__item">
                        <router-link to="/supplier-analysis">Supplier Analysis</router-link>
                    </p>
                </div>
            </div>

                <div class="list__item">
                    <p class="list__item--desc">
                        <router-link to="/reports">
                            <span class="desc">
                                <img class="main-icon img" src="@/assets/reports.png" alt="R">
                                <span class="name">Reports</span>
                            </span>
                        </router-link>
                    </p>
                </div>
            </span>
            <p class="list__title">Settings</p>
            <span v-if="userType === 'supplier'">
                <div class="list__item">
                    <p class="list__item--desc">
                        <router-link to="/supplier/home/profile">
                            <span class="desc">
                                <font-awesome-icon class="main-icon" icon="user" />
                                <span class="name">Profile</span>
                            </span>
                        </router-link>
                    </p>
                </div>
            </span>
            <span v-if="userType === 'client'">
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
                            <router-link to="/companies">Company Management</router-link>
                        </p>
                        <p class="dropdown-content__item">
                            <router-link to="/users">User Management</router-link>
                        </p>
                        <p class="dropdown-content__item">
                            <router-link to="/roles">Roles</router-link>
                        </p>
                        <p class="dropdown-content__item">
                            <router-link to="/company/tendersure">Tendersure</router-link>
                        </p>
                        <p class="dropdown-content__item">
                            <router-link to="/company/import/catalogue">Import Catalogue</router-link>
                        </p>
                        <p class="dropdown-content__item">
                            <router-link to="/company/import/gl">Import GL</router-link>
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
                            <router-link to="/gl-accounts">GL Accounts</router-link>
                        </p>
                        <p class="dropdown-content__item">
                            <router-link to="/tax-rates">Tax Management</router-link>
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
                            <img class="main-icon img" src="@/assets/workflow.png" alt="I">
                            <span class="name">Workflow</span>
                        </span>
                        <font-awesome-icon class="dropdown-icon" icon="chevron-right" />
                    </p>
                    <div class="list__item--dropdown dropdown-content">
                    <p class="dropdown-content__item">
                        <router-link to="/paths">Approval Path</router-link>
                    </p>
                    <p class="dropdown-content__item">
                        <router-link to="/route/requisition">Requisition Approval</router-link>
                    </p>
                    <p class="dropdown-content__item">
                        <router-link to="/route/purchase-order">PO Approval</router-link>
                    </p>
                    <p class="dropdown-content__item">
                        <router-link to="/route/invoice">Invoice Approval</router-link>
                    </p>
                    <p class="dropdown-content__item">
                        <router-link to="/route/items-capping">Items Capping Approval</router-link>
                    </p>
                    </div>
                </div>
                <!-- <div class="list__item">
                    <p class="list__item--desc">
                        <router-link to="/billing">
                            <span class="desc">
                                <font-awesome-icon class="main-icon" icon="money-bill-wave" />
                                <span class="name">Billing</span>
                            </span>
                        </router-link>
                    </p>
                </div> -->
            </span>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
    name: 'side-nav',
    data () {
        return {

        }
    },
    computed: {
        ...mapGetters('Company',['budgetModuleStatus']),
        ...mapGetters('User',['userType']),
    },
}
</script>

<style lang="scss" scoped>
.nav-side {
    width: 90%;
    height: 85vh;
    // background-color: $color-blue-main;
    background-color: $color-white-pure;
    // margin-top: -10vh;
    // @include right-shadow;
    z-index: -20;
    // overflow: hidden;
    border-right: 2px solid $color-gray-light;
    overflow-y: auto;
    overflow-x: hidden;
    @include scroll-bar;
    &::-webkit-scrollbar {
        width: $line-height/24;
        z-index: -20;
    }
}

.list {
    padding: $line-height/2 0;
    // padding-top: 15vh;
    // display: none;

    &__title {
        text-transform: uppercase;
        font-weight: 900;
        font-size: $line-height/2;
        color: $color-blue-medium;
        padding: 0 $line-height/1.5;
        margin-top: $line-height;
    }

    &__collapse {
        cursor: pointer;
        margin-bottom: $line-height/3;
        color: $color-blue-light;
        font-size: $line-height/1.2;
        @include shadow;
        text-align: right;
        float: right;
        // margin-right: -$line-height/3;
        z-index: 120;
        border-radius: 50%;


        &:hover {
            color: $color-blue-light;
        }
    }

    &__item {
        padding: 0 $line-height/2;
        margin: $line-height/1.5 0;
        cursor: pointer;
        font-size: $font-size-small;


        &--desc {

            color: $color-black-medium;
            // color: $color-blue-main;

            .desc {
                @include grid_row;
                justify-content: flex-start;

                .main-icon {
                    margin-right: $line-height/3;
                    width: $line-height;
                    // color: $color-blue-medium;
                }

                .img {
                    width: $line-height/1.1;
                }
            }

            &:hover {
                .name {
                    color: $color-blue-medium;
                }                
            }
        }

        .router-link-exact-active {
            .name {
                color: $color-blue-light;
            }            
        }
    }

    .dropdown {
        @include drop-down();
        display: block;

        .dropdown-icon {
            color: $color-green-main;
        }

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
}
</style>
