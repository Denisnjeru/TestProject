<template>
    <div class="side">
        <div class="actions">
            <p class="actions__title">Actions</p>
            <ol class="actions__list">
            <router-link to="/users">
                <li class="actions__list--item">Manage Users</li>
            </router-link>
            <router-link to="/user/create">
                <li class="actions__list--item">Create User</li>
            </router-link>
            <router-link to="/companies">
                <li class="actions__list--item">Import Users</li>
            </router-link>
            <li class="actions__list--item"></li>
            </ol>
        </div>
        <div class="statistics">

        </div>
    </div>
</template>

<style lang="scss" scoped>

</style>