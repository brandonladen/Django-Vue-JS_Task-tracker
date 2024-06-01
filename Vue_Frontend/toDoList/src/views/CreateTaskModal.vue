<template>
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <h2>Create Task</h2>
        <form @submit.prevent="submitTask">
          <div class="form-group">
            <label for="title">Title:</label>
            <input type="text" id="title" v-model="task.title" required>
          </div>
          <div class="form-group">
            <label for="description">Description:</label>
            <textarea id="description" v-model="task.description" required></textarea>
          </div>
          <button type="submit">Create Task</button>
          <button type="button" @click="$emit('close')">Close</button>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const props = defineProps({
    showModal: {
      type: Boolean,
      required: true
    }
  });
  
  const emit = defineEmits(['createTask', 'close']);
  
  const task = ref({ title: '', description: '' });
  
  const submitTask = () => {
    if (task.value.title && task.value.description) {
      emit('createTask', { title: task.value.title, description: task.value.description });
      task.value = { title: '', description: '' };
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
  </style>
  