<script setup>
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';
import axios from '../axiosConfig';
import CreateTaskModal from './CreateTaskModal.vue';
import EditTaskModal from './EditTaskModal.vue';

const store = useStore();
const router = useRouter();
const tasks = ref([]);
const isModalVisible = ref(false);
const editMode = ref(false);
const currentTask = ref(null);

onMounted(async () => {
  try {
    const response = await axios.get('/api/app/view/');
    tasks.value = response.data.results;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
});

const handleLogout = () => {
  store.dispatch('auth/logout');
  router.push('/login');
};

const showModal = () => {
  isModalVisible.value = true;

};

const closeModal = () => {
  isModalVisible.value = false;
};

const handleCreateTask = async (task) => {
  try {
    const userId = 1; 
    const newTask = {
      Title: task.title,
      Description: task.description,
      user: userId
    };
    const response = await axios.post('/api/app/view/', newTask);
    tasks.value.push(response.data);
    closeModal();
  } catch (error) {
    console.error('Error creating task:', error);
  }
};

const handleDeleteTask = async (taskId) => {
    try {
      await axios.delete(`/api/app/view/${taskId}/`);
      tasks.value = tasks.value.filter(task => task.id !== taskId);
    } catch (error) {
      console.error('Error deleting task:', error);
    }
  };

const editTask = (task) => {
  currentTask.value = {...task};
  editMode.value = true;
};

const closeEditModal = () => {
  editMode.value = false;
  currentTask.value = null;
};

const handleUpdateTask = async (updatedTask) => {
  try {
    const response = await axios.put(`/api/app/view/${updatedTask.id}/`, updatedTask);
    const index = tasks.value.findIndex(task => task.id === updatedTask.id);
    tasks.value[index] = response.data;
    closeEditModal();
    console.log('Task updated successfully!');
  } catch (error) {
    console.error('Error updating task:', error);
    console.log('Error updating task.');
  }
};
</script>

<template>
    <div class="app-container">
      <!-- Header -->
      <header class="header">
        <h1 class="#">TodoApp</h1>
        <button class="addtask_btn" @click="showModal">Add Task</button>
        <button class="logout_btn" @click="handleLogout">Logout</button>
      </header>
  
      <div class="heading">
        <h2>Bengohub Cohort One Task Manager</h2>
      </div>
  
      <!-- Main Content -->
      <div class="main-content">
        <div class="container mt-5 pt-5">
          <table class="custom-table">
            <thead>
              <tr>
                <th scope="col">Title</th>
                <th scope="col">Description</th>
                <th scope="col">Time Created</th>
                <th scope="col">Options</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="task in tasks" :key="task.id">
                <td>{{ task.Title }}</td>
                <td>{{ task.Description }}</td>
                <td>{{ task.Time_created }}</td>
                <td>
                  <button type="button" class="btn-primary" @click="editTask(task)">
                    <i class="fa fa-edit"></i> Edit
                  </button>
                  <br />
                  <button type="button" class="btn-danger"  @click="() => handleDeleteTask(task.id)">
                    <i class="fa fa-trash-o"></i> Delete
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
  
      <!-- Footer -->
      <footer class="footer">
        <p>2024 © All Rights Reserved | Designed and Developed by Bengo Hub</p>
      </footer>
  
      <CreateTaskModal :showModal="isModalVisible" @createTask="handleCreateTask" @close="closeModal" />
      <EditTaskModal v-if="editMode" :task="currentTask" @updateTask="handleUpdateTask" @close="closeEditModal" />
    </div>
  </template>

<style scoped>
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.cand {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  justify-content:  space-evenly;
}

.votcard {
  text-align: center;
  padding: 20px;
  border-radius: 10px;
  color: black;
}

.votcard:hover {
  transform: translateY(-5px);
}

img {
  height: 150px;
  width: 150px;
  object-fit: cover;
  border-radius: 50%;
  margin-bottom: 10px;
}

.vote-btn,
.view-btn, .logout_btn, .addtask_btn, .btn-primary {
  background-color: #3490dc;
  color: white;
  padding: 8px 16px;
  margin: 5px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.btn-danger {
background-color: red;
  color: white;
  padding: 8px 16px;
  margin: 5px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.vote-btn:hover,
.view-btn:hover {
  background-color: #2779bd;
}

.footer {
  text-align: center;
  padding: 10px;
  background-color: darkslategray;
  color: white;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #f0f0f0;
}

.main-content {
  flex-grow: 1;
}

.heading {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 50px;
}

.heading h2 {
  color: black;
  font-weight: bolder;
  font-size: xx-large;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  margin: 0;
}

.heading p {
  color: black;
  font-size: x-large;
}

/* Table atyling */

.container {
  max-width: 800px;
  margin: 0 auto; /* Centering the container */
  display: block; /* Ensuring it's a block-level element */
}

.custom-table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  font-size: 18px;
  text-align: left;
}

.custom-table thead tr {
  background-color: #343a40;
  color: #ffffff;
  text-align: left;
  border-bottom: 2px solid #dddddd;
}

.custom-table th,
.custom-table td {
  padding: 12px 15px;
  border: 1px solid #dddddd;
}

.custom-table tbody tr {
  border-bottom: 1px solid #dddddd;
}

.custom-table tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

.custom-table tbody tr:last-of-type {
  border-bottom: 2px solid #343a40;
}

.custom-table tbody tr:hover {
  background-color: #f1f1f1;
}

</style>
