<!-- filepath: /home/gazaboo/Documents/dev/test_python_O2Switch/vue_app/src/components/Users.vue -->
<template>
    <div class="users-container">
        <h1>Usersss Management</h1>
        <div class="users-list">
            <User v-for="user in users" :key="user.id" :user="user" />
        </div>

        <div class="new-user-form">
            <h2>Add New User</h2>
            <form @submit.prevent="createUser">
                <div class="form-group">
                    <label for="username">Username:</label>
                    <input type="text" id="username" v-model="newUser.username" required>
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" v-model="newUser.email" required>
                </div>
                <div class="form-group">
                    <label for="phone">Phone:</label>
                    <input type="text" id="phone" v-model="newUser.phone" required>
                </div>
                <div class="form-group">
                    <label for="address">Address:</label>
                    <input type="text" id="address" v-model="newUser.address" required>
                </div>
                <button type="submit" class="btn">Add User</button>
            </form>
        </div>
    </div>
</template>

<script>
import User from './User.vue';

export default {
    components: { User },
    data() {
        return {
            base: '/test_python', // on o2Switch
            // base: 'http://localhost:5000/',
            users: [],
            newUser: {
                username: '',
                email: '',
                phone: '',
                address: '',
                notes: ''
            }
        };
    },
    created() {
        this.fetchUsers();
    },
    methods: {
        async fetchUsers() {
            try {
                const response = await fetch(`${this.base}/users`);
                const data = await response.json();
                this.users = data.map(user => ({
                    ...user,
                    notes: user.notes || ''
                }));
            } catch (error) {
                console.error('Error fetching users:', error);
            }
        },
        async createUser() {
            try {
                const response = await fetch(`${this.base}/create_user`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(this.newUser)
                });
                if (response.ok) {
                    const newUser = await response.json();
                    this.users.push(newUser);
                    this.newUser = { username: '', email: '', phone: '', address: '', notes: '' };
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
.users-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Helvetica Neue', Arial, sans-serif;
}

h1 {
    text-align: center;
    color: #4f6e8d;
    margin-bottom: 30px;
}

.users-list {
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.new-user-form {
    margin-top: 40px;
    background-color: #747d80;
    padding: 20px;
    border-radius: 8px;
}

.new-user-form h2 {
    color: #2c3e50;
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 15px;
}

.form-group label {
    display: block;
    font-weight: 600;
    margin-bottom: 5px;
    color: #34495e;
}

.form-group input {
    width: 100%;
    padding: 8px 12px;
    border: 1px solid #bdc3c7;
    border-radius: 4px;
    font-size: 1rem;
    color: #2d3436;
}

.btn {
    background-color: #3498db;
    color: #ffffff;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.2s ease;
}

.btn:hover {
    background-color: #2980b9;
}
</style>