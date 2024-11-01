import { createStore } from 'vuex';
import createPersistedState from "vuex-persistedstate";
export default createStore({
    state: {
      refresh: null,
      access: null,
      isDark: false,
      conversation:[],
      conversation_uuid:null,
      settings:{
        pitch:1,
        volume:1,
        rate:0.8,
        selectedVoice:null,
        continueVoice:false,
      }
    },
    getters: {
        refresh: state => state.refresh,
        access: state => state.access,
        conversation: state => state.conversation,
        isDark: state => state.isDark,
        conversation_uuid: state => state.conversation_uuid,
        settings: state => state.settings,
  
    },
    mutations: {
      setRefresh(state, refresh) {
        state.refresh = refresh;
      },
      setAccess(state, access) {
        state.access = access;
      },
      setConversation(state, conversation) {
        state.conversation = conversation;
      },
      
      setIsDark(state, isDark) {  // Renamed from isDark to setIsDark
        state.isDark = isDark;
      },
      setConversationUUID(state, convo){
        state.conversation_uuid = convo
      },
      setSettings(state, settings){
        state.settings = settings;
      },
      resetStore(state) {
        state.refresh = null;
        state.access = null;
        state.isDark = false;
        state.conversations = [];
       state.conversation_uuid=null;
       state.settings={
            pitch:1,
            volume:1,
            rate:0.8,
            selectedVoice:null,
            continueVoice:false,
          };
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
  