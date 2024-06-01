<template>
  <div class="modal">
    <div class="modal-content">
      <h2>Edit Task</h2>
      <form @submit.prevent="submitTask">
        <div class="form-group">
          <label for="editTitle">Title:</label>
          <input type="text" id="editTitle" v-model="editedTask.Title" required>
        </div>
        <div class="form-group">
          <label for="editDescription">Description:</label>
          <textarea id="editDescription" v-model="editedTask.Description" required></textarea>
        </div>
        <button type="submit">Update Task</button>
        <button type="button" @click="$emit('close')">Close</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
  task: {
    type: Object,
    required: true
  }
});

const emit = defineEmits(['updateTask', 'close']);

const editedTask = ref({ ...props.task });

watch(() => props.task, (newTask) => {
  editedTask.value = { ...newTask };
}, { immediate: true });

const submitTask = () => {
  if (editedTask.value.Title && editedTask.value.Description) {
    emit('updateTask', { ...editedTask.value });
  }
};
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  max-width: 500px;
  width: 100%;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 10px;
  box-sizing: border-box;
}

button {
  margin-top: 10px;
  padding: 10px 20px;
  background-color: #3490dc;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #2779bd;
}

button[type="submit"] {
  background-color: green;
}

button[type="submit"]:hover {
  background-color: darkgreen;
}

button[type="button"] {
  background-color: red;
}

button[type="button"]:hover {
  background-color: darkred;
}
</style>
