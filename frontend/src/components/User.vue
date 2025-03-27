<template>
    <div class="user-card">
        <div class="info">
            <div class="header">
                <h2>{{ user.username }}</h2>
                <p class="email">{{ user.email }}</p>
            </div>
            <div class="details">
                <p><strong>Phone:</strong> {{ user.phone }}</p>
                <p><strong>Address:</strong> {{ user.address }}</p>
            </div>
        </div>
        <div class="notes">
            <textarea v-model="editableNotes" @change="updateNotes" placeholder="Notes..."></textarea>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        user: { type: Object, required: true }
    },
    data() {
        return {
            editableNotes: this.user.notes || ''
        };
    },
    methods: {
        async updateNotes() {
            try {
                const response = await fetch(`/test_python/update_user/${this.user.id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ notes: this.editableNotes })
                });
                if (!response.ok) {
                    console.error('Error updating notes:', response.statusText);
                }
            } catch (error) {
                console.error('Error updating notes:', error);
            }
        }
    }
};
</script>

<style scoped>
.user-card {
    display: flex;
    flex-direction: row;
    align-items: center;
    border-radius: 8px;
    background-color: #d7d7d7;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    padding: 10px;
    margin: 10px 0;
}

.info {
    flex: 2;
    display: flex;
    flex-direction: column;
}

.header {
    margin-bottom: 5px;
}

.header h2 {
    margin: 0;
    font-size: 1.1rem;
    color: #2c3e50;
}

.header .email {
    margin: 0;
    font-size: 0.85rem;
    color: #7f8c8d;
}

.details p {
    margin: 3px 0;
    font-size: 0.9rem;
    color: #34495e;
}

.notes {
    flex: 1;
    margin-left: 10px;
}

.notes textarea {
    width: 100%;
    height: 60px;
    padding: 6px;
    border: 1px solid #bdc3c7;
    border-radius: 4px;
    font-size: 0.9rem;
    resize: none;
}
</style>