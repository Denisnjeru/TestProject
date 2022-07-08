<template>
    <div class="side">
        <div class="actions">
            <p class="actions__title">Actions</p>
            <ol class="actions__list">
                <router-link to="/supplier/home/issued-items">
                    <li class="actions__list--item">Goods Issued</li>
                </router-link>
                <router-link to="/supplier/home/issue-items">
                    <li class="actions__list--item">Issue Goods</li>
                </router-link>
            </ol>
        </div>
        <div class="statistics">

        </div>
    </div>
</template>

<style lang="scss" scoped>

</style>