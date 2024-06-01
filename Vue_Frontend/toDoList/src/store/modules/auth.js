// src/store/auth/auth.js
import axios from '@/axiosConfig';

const state = {
  isAuthenticated: false,
  user: null,
};

const mutations = {
  SET_AUTHENTICATED(state, isAuthenticated) {
    state.isAuthenticated = isAuthenticated;
  },
  SET_USER(state, user) {
    state.user = user;
  },
};

const actions = {
  async login({ commit }, payload) {
    try {
      const response = await axios.post('/api/login/', payload);
      // Extract the access token and user data from the response
      const token = response.data.token;
      const user = {
        userid: response.data.id,
        username: response.data.username,
        email: response.data.email,
      };

      // Set the access token in session storage
      sessionStorage.setItem('token', token);

      // Commit the mutations
      commit('SET_AUTHENTICATED', true);
      commit('SET_USER', user);

      return true;
    } catch (error) {
      // Handle login error
      console.error('Login failed:', error.message);
      throw new Error('An error occurred during login.');
    }
  },

  logout({ commit }) {
    // Remove access token from session storage
    sessionStorage.removeItem('token');

    // Clear authentication state
    commit('SET_AUTHENTICATED', false);
    commit('SET_USER', null);
  },

  checkAuthentication({ commit }) {
    const token = sessionStorage.getItem('token');
    
    // Check if access token exists
    if (token) {
      // Set authentication state
      commit('SET_AUTHENTICATED', true);
      
      // Fetch user information if needed
      // This part assumes you have an endpoint to get user info by token
      axios.get('/api/user/', { headers: { Authorization: `Token ${token}` } })
        .then(response => {
          const user = {
            username: response.data.username,
            email: response.data.email,
          };
          commit('SET_USER', user);
        })
        .catch(() => {
          // Handle error, maybe token is invalid
          commit('SET_AUTHENTICATED', false);
          commit('SET_USER', null);
        });
    }
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
