<template>
    <div>
        <h1>Users</h1>
        <ul>
            <li v-for="user in users" :key="user.id">
                {{ user.username }} ({{ user.email }})
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            users: []
        };
    },
    created() {
        this.fetchUsers();
    },
    methods: {
        async fetchUsers() {
            try {
                const response = await fetch('/users');
                const data = await response.json();
                this.users = data;
            } catch (error) {
                console.error('Error fetching users:', error);
            }
        }
    }
};
</script>

<style scoped>
/* Add any styles you need here */
</style>