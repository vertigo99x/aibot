import { createStore } from 'vuex';
import createPersistedState from "vuex-persistedstate";
export default createStore({
    state: {
      refresh: null,
      access: null,
      isDark: false,
      conversation:[
        {
          isUser: false,
          text: 'Hey there!',
          timestamp: new Date()
        }
      ],
    },
    getters: {
        refresh: state => state.refresh,
        access: state => state.access,
        conversation: state => state.conversation,
        isDark: state => state.isDark,
    },
    mutations: {
      setRefresh(state, refresh) {
        state.refresh = refresh;
      },
      setAccess(state, access) {
        state.access = access;
      },
      setConversations(state, conversations) {
        state.conversations = conversations;
      },
      
      setIsDark(state, isDark) {  // Renamed from isDark to setIsDark
        state.isDark = isDark;
      },
      resetStore(state) {
        state.refresh = null;
        state.access = null;
        state.isDark = false;
        state.conversations = [];
       
      },
    },
    actions: {
    },
    modules: {
    },
    plugins: [
      createPersistedState({
        // Options to configure persistence
        storage: window.sessionStorage, //window.localStorage,
      })
    ]
  })
  