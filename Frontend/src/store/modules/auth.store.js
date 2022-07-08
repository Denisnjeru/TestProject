import auth from '../../services/authentication';
import Utils from '../../utils/Cookies';

const initialState = () => ({
  authStatus: 0, // 1 - Loading, 2 - Successful, 3 - unsuccesful
  authMessage: null,
  token: (Utils.authTokenExists() && Utils.getToken()) || '',
  authUser: null, //(Utils.authTokenExists()) || [],
  authError: null,

});

const state = initialState();

const getters = {
  authStatus: state => state.authStatus,
  authMessage: state => state.authMessage,
  isAuthenticated(state) {
      return !!state.token
  },
  authUser(state) {
      return state.authUser
  },
  authError(state) {
      return state.authError
  }

}

const mutations = {
  authRequest(state) {
    state.authStatus = 1
  },
  authSuccess(state, response) {
    state.authStatus = 2
    state.authMessage = 'Logged in successfully'
    state.token = response.token.access
    state.authUser = response.decodedToken
    // do domething with the response
  },
  authError(state, error) {
    state.authStatus = 3
    state.authError = error
  },
  authLogout(state, response){
    state.authStatus = 0
    state.authMessage = null
    state.isAuthenticated = false
    state.token = ''
    state.authUser = []
  },
  updateToken(state, token) {
    state.token = token
  },
  
  // Reset
  reset(state) {
    const newState = initialState()
    Object.keys(newState).forEach(key => {
        state[key] = newState[key]
    })
  }
}

const actions = {
  login: async ({ commit }, payload) => {
    try {
      commit('authRequest')
      const response = await auth.login(payload);
      let userData = Utils.saveToken(response.data);
      commit('authSuccess', userData);
    } catch (err) {
      let error = err.response.data.detail
      commit('authError', error)
    }
  },
  setToken({ commit }, payload) {
    let userData = Utils.setToken(payload);
    commit('authSuccess', userData);
    commit('updateToken', payload);
  },
  logout({ commit }){
    Utils.removeToken('userData')
    Utils.removeToken('token')
    commit('reset')
  },
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}