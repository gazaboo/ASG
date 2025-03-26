<template>
    <div>
        <h1>Users</h1>
        <ul>
            <li v-for="user in users" :key="user.id">
                {{ user.username }} ({{ user.email }})
            </li>
        </ul>

        <h2>Add New User</h2>
        <form @submit.prevent="createUser">
            <div>
                <label for="username">Username:</label>
                <input type="text" id="username" v-model="newUser.username" required>
            </div>
            <div>
                <label for="email">Email:</label>
                <input type="email" id="email" v-model="newUser.email" required>
            </div>
            <button type="submit">Add User</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            users: [],
            newUser: {
                username: '',
                email: ''
            }
        };
    },
    created() {
        this.fetchUsers();
    },
    methods: {
        async fetchUsers() {
            try {
                const response = await fetch('/test_python/users');
                const data = await response.json();
                this.users = data;
            } catch (error) {
                console.error('Error fetching users:', error);
            }
        },
        async createUser() {
            try {
                const response = await fetch('/test_python/create_user', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.newUser)
                });
                if (response.ok) {
                    const newUser = await response.json();
                    this.users.push(newUser);
                    this.newUser.username = '';
                    this.newUser.email = '';
                } else {
                    console.error('Error creating user:', response.statusText);
                }
            } catch (error) {
                console.error('Error creating user:', error);
            }
        }
    }
};
</script>

<style scoped>
/* Add any styles you need here */
form {
    margin-top: 20px;
}

form div {
    margin-bottom: 10px;
}

form label {
    margin-right: 10px;
}

form input {
    padding: 5px;
}

button {
    padding: 5px 10px;
}
</style>