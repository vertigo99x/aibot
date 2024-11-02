<template>
    <main>
      
        <div class="sidebar" :class="{'closed':!isSidebarOpen}">
            <div class="menu" v-if="!isBig()">
                <button @click="isSidebarOpen = !isSidebarOpen" :class="{'rotatemenu':!isSidebarOpen}"><svg xmlns="http://www.w3.org/2000/svg" height="36px" viewBox="0 -960 960 960" width="24px" fill="#F44335"><path d="M360-120v-720h80v720h-80Zm160-160v-400l200 200-200 200Z"/></svg></button>
                </div>
          <div class="top-section" v-if="isBig() || (!isBig() && isSidebarOpen)" >
            
            <button style="padding:.5rem" @click="createNewConversation()"><span >New Conversation</span>
              <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M440-440H200v-80h240v-240h80v240h240v80H520v240h-80v-240Z"/></svg></button>
          
             
            </div>

          <div class="next-section">
            
            <button style="padding:.5rem" @click="showSettingsModal=true"><span ></span>
          <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M440-120v-240h80v80h320v80H520v80h-80Zm-320-80v-80h240v80H120Zm160-160v-80H120v-80h160v-80h80v240h-80Zm160-80v-80h400v80H440Zm160-160v-240h80v80h160v80H680v80h-80Zm-480-80v-80h400v80H120Z"/></svg>
          </button>
          <button class="logout" style="background-color: transparent;" @click="logout()">
            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h280v80H200v560h280v80H200Zm440-160-55-58 102-102H360v-80h327L585-622l55-58 200 200-200 200Z"/></svg></button>
        
                    
             
            </div>
            
          <div class="conversations">
            <h3>Recent Conversations</h3>
            <div class="conversation__item" v-for="convo in conversation_list" :key="convo" style="cursor:pointer;" @click="getConversations(convo.uuid)">
              <div class="conversation__item__details">
                <div class="conversation__item__details__last-message" :class="{'active':conversation_uuid==convo.uuid}">{{convo.conversation_title.replace("##", '')}}</div>
              </div>
            </div>
           
            
           
          </div>
        </div>
        <div class="--dark-theme" id="chat">
            <div class="menu" v-if="!isBig()">
                <button @click="isSidebarOpen = !isSidebarOpen" :class="{'rotatemenu':!isSidebarOpen}"><svg xmlns="http://www.w3.org/2000/svg" height="36px" viewBox="0 -960 960 960" width="24px" fill="#F44335"><path d="M360-120v-720h80v720h-80Zm160-160v-400l200 200-200 200Z"/></svg></button>
              </div>
          <div class="chat__conversation-board" ref="conversationBoard">
            
            <div class="chat__conversation-board__message-container" v-for="item in conversation" :key="item" :class="{'reversed':item.isUser}">
              <div class="chat__conversation-board__message__person">
                <div class="chat__conversation-board__message__person__avatar">
                  <img v-if="item.isUser" :src="userAvatar" alt=""/>
                  <img v-else src="https://th.bing.com/th/id/OIP.epmj6On8bW5ajB4jOlZeEAHaE7?rs=1&pid=ImgDetMain" alt=""/>
                </div><span class="chat__conversation-board__message__person__nickname">AI Buddy</span>
              </div>
              <div class="chat__conversation-board__message__context">
                <div class="chat__conversation-board__message__bubble"> <span v-html="item.text.replace(/\n/g, '<br>')"></span></div>
              </div>
              <div class="chat__conversation-board__message__options">
                <button class="btn-icon chat__conversation-board__message__option-button option-item emoji-button">
                  <svg class="feather feather-smile sc-dnqmqq jxshSx" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                    <circle cx="12" cy="12" r="10"></circle>
                    <path d="M8 14s1.5 2 4 2 4-2 4-2"></path>
                    <line x1="9" y1="9" x2="9.01" y2="9"></line>
                    <line x1="15" y1="9" x2="15.01" y2="9"></line>
                  </svg>
                </button>
                <button class="btn-icon chat__conversation-board__message__option-button option-item more-button">
                  <svg class="feather feather-more-horizontal sc-dnqmqq jxshSx" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                    <circle cx="12" cy="12" r="1"></circle>
                    <circle cx="19" cy="12" r="1"></circle>
                    <circle cx="5" cy="12" r="1"></circle>
                  </svg>
                </button>
              </div>
            </div>

            <div class="new-convo" v-if="conversation.length == 0">
                <h3 class="">Type a text or use the Microphone button to Begin</h3>
            </div>
           

           
            <div class="chat__conversation-board__message-container typing" v-if="isLoading">
              <div class="chat__conversation-board__message__person">
                <div class="chat__conversation-board__message__person__avatar"><img src="https://th.bing.com/th/id/OIP.epmj6On8bW5ajB4jOlZeEAHaE7?rs=1&pid=ImgDetMain" alt=""/></div><span class="chat__conversation-board__message__person__nickname">Dennis Mikle</span>
              </div>
              <div class="chat__conversation-board__message__context">
                <div class="chat__conversation-board__message__bubble" style="background:#ababab">
                    <div class="ellipsis one"></div>
                    <div class="ellipsis two"></div>
                    <div class="ellipsis three"></div>
                </div>
              </div>
              <div class="chat__conversation-board__message__options">
                <button class="btn-icon chat__conversation-board__message__option-button option-item emoji-button">
                  <svg class="feather feather-smile sc-dnqmqq jxshSx" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                    <circle cx="12" cy="12" r="10"></circle>
                    <path d="M8 14s1.5 2 4 2 4-2 4-2"></path>
                    <line x1="9" y1="9" x2="9.01" y2="9"></line>
                    <line x1="15" y1="9" x2="15.01" y2="9"></line>
                  </svg>
                </button>
                <button class="btn-icon chat__conversation-board__message__option-button option-item more-button">
                  <svg class="feather feather-more-horizontal sc-dnqmqq jxshSx" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                    <circle cx="12" cy="12" r="1"></circle>
                    <circle cx="19" cy="12" r="1"></circle>
                    <circle cx="5" cy="12" r="1"></circle>
                  </svg>
                </button>
              </div>
            </div>
          </div>
          <div class="chat__conversation-panel">
            <div class="chat__conversation-panel__container">
              <button class="chat__conversation-panel__button panel-item btn-icon add-file-button" @click="downloadConversation">
               
<svg xmlns="http://www.w3.org/2000/svg" height="36px" viewBox="0 -960 960 960" width="36px" fill="#e8eaed"><path d="M480-320 280-520l56-58 104 104v-326h80v326l104-104 56 58-200 200ZM240-160q-33 0-56.5-23.5T160-240v-120h80v120h480v-120h80v120q0 33-23.5 56.5T720-160H240Z"/></svg>
              </button>
              
              <input class="chat__conversation-panel__input panel-item" placeholder="Type a message..." v-model="searchText" @keypress.enter="sendTextToApi(searchText)">
              <button class="chat__conversation-panel__button panel-item btn-icon send-message-button" style="background:#4CAF50;" v-if="!isSpeaking" @click="toggleListening()">
                
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M480-400q-50 0-85-35t-35-85v-240q0-50 35-85t85-35q50 0 85 35t35 85v240q0 50-35 85t-85 35Zm0-240Zm-40 520v-123q-104-14-172-93t-68-184h80q0 83 58.5 141.5T480-320q83 0 141.5-58.5T680-520h80q0 105-68 184t-172 93v123h-80Zm40-360q17 0 28.5-11.5T520-520v-240q0-17-11.5-28.5T480-800q-17 0-28.5 11.5T440-760v240q0 17 11.5 28.5T480-480Z"/></svg>
              </button>
              <button class="chat__conversation-panel__button panel-item btn-icon send-message-button" style="background:#F44335;" v-else @click="stopSpeech()">
                
                
<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="m136-304-92-90q-12-12-12-28t12-28q88-95 203-142.5T480-640q118 0 232.5 47.5T916-450q12 12 12 28t-12 28l-92 90q-11 11-25.5 12t-26.5-8l-116-88q-8-6-12-14t-4-18v-114q-38-12-78-19t-82-7q-42 0-82 7t-78 19v114q0 10-4 18t-12 14l-116 88q-12 9-26.5 8T136-304Zm104-198q-29 15-56 34.5T128-424l40 40 72-56v-62Zm480 2v60l72 56 40-38q-29-26-56-45t-56-33Zm-480-2Zm480 2Z"/></svg>  </button>
              <button class="chat__conversation-panel__button panel-item btn-icon send-message-button" @click="sendTextToApi(searchText)">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" data-reactid="1036">
                  <line x1="22" y1="2" x2="11" y2="13"></line>
                  <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                </svg>
              </button>
            </div>
          </div>
          <div class="modal" v-if="isListening">
            <div class="modal-content">
              <img :src="animation" alt="" @click="toggleListening(true)">
              <p>{{transcription}}</p>
            </div>
          </div>

          <div class="modal settings" v-if="showSettingsModal">
            <div class="modal-content">
              <button class="back" @click="showSettingsModal=false">Close</button>
              <div class="top-level">
                <h3 class="title">Voice Settings</h3>
              </div>
              <div class="top">
                <h3>Voice</h3>
                <select name="" id="" v-model="voice" @change="selectedVoice=item;updateSettings()">
                  <option :value="item.name" v-for="item in voices" :key="item">{{item.name}}</option>
                </select>
              </div>
              <div class="sliders">
                <div class="setting-item">
                  <h3 class="setting_title">Pitch</h3>
                  <input type="range" name="" id="" class="range" min="0" max="2" step="0.1" v-model="pitch" @input="updateSettings()">
                  <h3 class="setting_title">{{pitch}}</h3>
                </div>
                <div class="setting-item">
                  <h3 class="setting_title">Rate</h3>
                  <input type="range" name="" id="" class="range" min="0" max="10" step="0.1" v-model="rate" @input="updateSettings()">
                  <h3 class="setting_title">{{rate}}</h3>
                </div>
                <div class="setting-item">
                  <h3 class="setting_title">volume</h3>
                  <input type="range" name="" id="" class="range" min="0" max="1" step="0.1" v-model="volume" @input="updateSettings()">
                  <h3 class="setting_title">{{volume * 100}}%</h3>
                </div>
                <div class="" style="display:flex;">
                  <h3>Enable Continous Voice</h3>
                  <input type="checkbox" class="checkbox" v-model="continueVoice" @change="updateSettings()">
                </div>
              </div>
            </div>
          </div>
        </div>
       </main>
</template>

<script setup>
import { ref, onMounted, inject, watch } from 'vue';
import animation from '../assets/animation.gif'; 
import userAvatar from "../assets/20a766d6-8149-4669-baf1-de1b6f281a90.jpeg"
import axios from 'axios'
import { useStore } from 'vuex';
import { useRouter, useRoute } from 'vue-router';
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

const store = useStore();
const synth = window.speechSynthesis;
const router = useRouter();
const $http = inject('$http');


const conversation = ref(store.getters.conversation);
const conversation_list = ref(null);
const isListening = ref(false);
const showSettingsModal = ref(false);
const isLoading = ref(false);
const searchText = ref('');
const transcription = ref(''); 
const isSidebarOpen = ref(false);
const isSpeaking = ref(false);
const userData = ref(null);
const conversationBoard = ref(null);
let recognition;

const voices = ref([]);
const voice = ref(null);
const selectedVoice = ref(store.getters.selectedVoice);
const pitch = ref(store.getters.settings.pitch); 
const volume = ref(store.getters.settings.volume); 
const rate = ref(store.getters.settings.rate); 
const continueVoice = ref(store.getters.settings.continueVoice); 
const conversation_uuid = ref(store.getters.conversation_uuid);

const CUSTOM_API = "http://165.154.252.219/service/"


watch(() => store.getters.conversation_uuid, (newVal) => {
  conversation_uuid.value = newVal;
}, { immediate: true });



const updateSettings = () => {
  store.commit('setSettings', {
        pitch:pitch.value,
        volume: volume.value,
        rate: rate.value,
        selectedVoice:selectedVoice.value,
        continueVoice:continueVoice.value
      })
}

function stopSpeech() {
    speechSynthesis.cancel();
    isSpeaking.value = false;
}


const downloadConversation = () =>  {
      if(conversation.value){

        let textContent = "";
        for(let x = 0; x<conversation.value.length; x++){
          let title = conversation.value[x].isUser ? "You: " : "Assistant/Bot: " 
          textContent += title + conversation.value[x].text + "\n";
        }

        const blob = new Blob([textContent], { type: "text/plain" });

        const url = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = url;
        link.download = "chat" + conversation_uuid.value + ".txt"; 
        link.click();
        URL.revokeObjectURL(url);
      }
      
}

      function speak(text) {
      try{
        if ('speechSynthesis' in window) {
          const utterance = new SpeechSynthesisUtterance(text);

   
          // Optional: Set voice properties to sound more human-like
          utterance.pitch = pitch.value; // Range: 0 (low) to 2 (high)
          utterance.rate = rate.value; // Range: 0.1 (slow) to 10 (fast)
          utterance.volume = volume.value; // Range: 0 (mute) to 1 (full volume)

          // Select a human-like voice, if available
          const voices = speechSynthesis.getVoices();
          try{
            utterance.voice = voice.value ? selectedVoice.value : voices.value.find(voice => voice.name.includes('Google US English')) || voices.value[2];
          } catch (error){
            utterance.voice = voices.find(voice => voice.name.includes('Google US English')) || voices[2];
         
          }
          
          // Speak the text
          
          speechSynthesis.speak(utterance);
          isSpeaking.value = true;

          /*
          window.speechSynthesis.onvoiceschanged = function() {
          const voices = speechSynthesis.getVoices();
          console.log(voices);  
          };*/

          utterance.onend = (() => {
            isSpeaking.value = false;
            if(continueVoice.value){
              isLoading.value=true;
              toggleListening();
            }
          })

      } else {
        alert('Sorry, your browser does not support text-to-speech.');
      }
      } catch(error){
        console.log(error);
      }
        }



const logout = () => {
  store.commit('resetStore');
   router.push('/login');
}

        
async function refreshToken(callback) {
    try {
        const response = await $http.post('api/token/refresh', {
            refresh: store.getters.refresh,
        });

        if (response.data.access) {
            store.commit('setAccess', response.data.access);
            axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
            await callback();  
        } else {
            router.push('/login');  
        }
    } catch (error) {
        console.error('Failed to refresh token', error);
        router.push('/login');  
    }
}

function scrollToBottom() {

  if (conversationBoard.value) {
    conversationBoard.value.scrollTo({
      top: conversationBoard.value.scrollHeight,
      behavior: 'smooth' // Enables smooth scrolling
    });
  }
}





const isBig = () => {
    return window.innerWidth > 768;
}

const toggleListening = (forceStop=false) => {
  if(forceStop){
    isLoading.value=false;
  }
  if (isListening.value || forceStop) {
    recognition.stop();
    isListening.value = false;
  } else {
    transcription.value = '';
    isListening.value = true;
    recognition.start();
  }
};

async function getUserData(){
  try {
        const response = await $http.get('accounts/userdata/');
        userData.value = response.data;
    } catch (error) {
   
        if (error.response) {
            const status = error.response.status;
            if (status === 401) {
                
                await refreshToken(getUserData);
            } else {
            
                console.error(`Error ${status}: ${error.response.data.message}`);
                toast.error(`Error ${status}: ${error.response.data.message}`, {
                    autoClose: 3000,
                    position: toast.POSITION.TOP_RIGHT,
                });
            }
        } else if (error.request) {
           
            console.error('No response received:', error.request);
            toast.error('No response received. Please try again later.', {
                autoClose: 3000,
                position: toast.POSITION.TOP_RIGHT,
            });
        } else {
        
            console.error('Error', error);
            toast.error(`Error: ${error.message}`, {
                autoClose: 3000,
                position: toast.POSITION.TOP_RIGHT,
            });
        }
    }
}


const createNewConversation = () => {
  conversation.value=[];
  conversation_uuid.value = null;
  store.commit('setConversation', conversation.value);
  store.commit('setConversationUUID',conversation_uuid.value)
}


async function getConversations(uuid=null){
  try {
      const params = {
        uuid:uuid
      }
        const response = await $http.get('api/v1/conversations/', {params});
        if(uuid){
          conversation.value = response.data.conversation_list;
          conversation_uuid.value = uuid;
          store.commit('setConversation', conversation.value);
          
        } else {
          conversation_list.value = response.data

        }
        
        
    } catch (error) {
   
        if (error.response) {
            const status = error.response.status;
            if (status === 401) {
                
                await refreshToken(getConversations);
            } else {
            
                console.error(`Error ${status}: ${error.response.data.message}`);
                toast.error(`Error ${status}: ${error.response.data.message}`, {
                    autoClose: 3000,
                    position: toast.POSITION.TOP_RIGHT,
                });
            }
        } else if (error.request) {
           
            console.error('No response received:', error.request);
            toast.error('No response received. Please try again later.', {
                autoClose: 3000,
                position: toast.POSITION.TOP_RIGHT,
            });
        } else {
        
            console.error('Error', error);
            toast.error(`Error: ${error.message}`, {
                autoClose: 3000,
                position: toast.POSITION.TOP_RIGHT,
            });
        }
    }
    setTimeout(() => {
      scrollToBottom();
    },500)
}

async function updateConversion(isNew=false, data=null){
  if(isNew){
    const response = await $http.post('api/v1/conversations/', data);
    console.log(response.data)
    conversation_uuid.value = response.data.uuid;
    store.commit('setConversationUUID',conversation_uuid.value)
    return ;
  }
  const response = await $http.put('api/v1/conversations/', data);
  return ;
}

const sendTextToApi = async (text) => {
   if(text.trim().length > 1){
    searchText.value = '';
    conversation.value.push({
      text: text,
      isUser: true,
    });
    scrollToBottom();
    store.commit('setConversation', conversation.value);
    isLoading.value = true;
    
  try {
    const data = {
      text:text,
      conversation_list:conversation_uuid.value ? conversation.value : []
    }

    const response = await $http.post(CUSTOM_API + 'api/v1/getResponse', data);
    console.log(response.data)

    
    let result=response.data.response.split("|sep|");
    let title = null;

    if(result.length > 1) {
      title = result[0];
      result = result[1]
    } else{
      result = response.data.response
    }
    isLoading.value=false;
    conversation.value.push({
      text: result,
      isUser: false,
    });
    scrollToBottom();
    if(!conversation_uuid.value){
      updateConversion(true, {
        conversation_list:conversation.value,
        conversation_title:title ? title : text.slice(0, 30)
      })
    } else {
      updateConversion(false, {
        uuid:conversation_uuid.value,
        conversation_list:conversation.value,
        conversation_title:title ? title : text.slice(0, 30)
      })
    }
    
    speak(result);
    store.commit('setConversation', conversation.value);
    
    
  } catch (error) {
    console.error('Error fetching API:', error);
  }
   }
};

onMounted(() => {

  getUserData();
  getConversations();

  window.speechSynthesis.onvoiceschanged = function() {
      const myVoices = speechSynthesis.getVoices();
      voices.value = myVoices
      const myselectedVoice = myVoices.find(voice => voice.name.includes('Google US English')) || myVoices[2];
      const voiceName = myselectedVoice ? myselectedVoice.name : 'Default Voice';
      selectedVoice.value = myselectedVoice;
      voice.value = voiceName;
      updateSettings();
      };


  if (!('webkitSpeechRecognition' in window)) {
    alert('Your browser does not support speech recognition.');
    return;
  }

  recognition = new window.webkitSpeechRecognition();
  recognition.lang = 'en-US'; 
  recognition.interimResults = true;
  recognition.continuous = false;

  
  recognition.onresult = (event) => {
    transcription.value = Array.from(event.results)
      .map(result => result[0].transcript)
      .join('');
  };

 
  recognition.onend = async () => {
    isListening.value = false;
    if (transcription.value) {
      await sendTextToApi(transcription.value);
    }
  };
});


</script>

<style lang="scss" scoped>



.--dark-theme {
  --chat-background: transparent /*rgba(10, 14, 14, 0.75);*/;
  --chat-panel-background: #131719;
  --chat-bubble-background: #1b2124;
  --chat-add-button-background: #212324;
  --chat-send-button-background: #8147fc;
  --chat-text-color: #a3a3a3;
  --chat-options-svg: #a3a3a3;
}

body {
  
  margin:0;
  padding:0;
  scroll-behavior:smooth;
}


.modal{
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;

  

  .modal-content{
    background: transparent;
    padding: 2rem;
    border-radius: 10px;
    max-width: 500px;
    display: flex;
    flex-direction: column;
    align-items: center;

    img{
      width: 150px;
      height: auto;
      margin-bottom: 2rem;
      
    }

    p{
      font-size: 18px;
      text-align: center;
      color:#fff;
      background:#a3a3a3;
      font-size:24px;
      padding:1rem;
    }
  }

  &.settings{

    .modal-content{
      background:#1b2124;
      width:100%;
      max-width: 30rem;
      justify-content: flex-start;
      align-items:center;
      display: flex;
      height:100%;
      max-height:fit-content;
      position: relative;
      animation:fadein .3s ease forwards;
      opacity: 0;

      .back{
        position: absolute;
        top: 1rem;
        left: 1rem;
        cursor: pointer;
        background:#F44335;
        color:#fff;
        border:1px solid #F44335;
        padding:.5rem 1rem;
        border-radius: .5rem;
      }

      h3{
        color: #ababab;
        font-size: 14px;
        &.title{
          font-size:18px;
          color:#fff;
        }
      }
      select{
        padding:.5rem;
        font-size: 16px;
        font-weight: bold;
        border-radius: .5rem;
      }

      .top{
        display: grid;

        padding: 1rem 0;
        border-bottom: 1px solid #333;
      }
      .sliders{
        display:flex;
        flex-direction: column;
        width:100%;
       

        .setting-item{
          display:grid;
          grid-auto-flow: column;
          grid-template-columns: 15% 60% auto;
          gap:1rem;
          
        }

        input[type='range'] {
          
          width: 100%;
        }
        input[type="checkbox"]{
          width:1.2rem;
        }
        
        

      }
      
    }
  }
}

.chat__conversation-board__message-container{
  padding:0 2rem;
}

/* Styling the scrollbar for the conversation board */
.chat__conversation-board::-webkit-scrollbar, .conversations::-webkit-scrollbar {
  width: 8px; /* Width of the scrollbar */
}

.chat__conversation-board::-webkit-scrollbar-track, .conversations::-webkit-scrollbar-track {
  background: rgba(0,0,0,0.7); /* Background of the scrollbar track */
}

.chat__conversation-board::-webkit-scrollbar-thumb, .conversations::-webkit-scrollbar-thumb {
  background-color: #8147fc; /* Color of the scrollbar thumb */
  border-radius: 4px; /* Rounded corners */
  border: 2px solid rgba(0,0,0,0.7); /* Optional border */
}

.chat__conversation-board::-webkit-scrollbar-thumb:hover .conversations::-webkit-scrollbar-thumb:hover {
  background-color: #555; /* Color on hover */
}

/* Firefox scrollbar styling */
.chat__conversation-board, .conversations {
  scrollbar-width: thin; /* Makes the scrollbar thinner */
  scrollbar-color: #8147fc rgba(0,0,0,0.7); /* thumb color and track color */
}



.new-convo{
  width:100%;
  height:100%;
  display: grid;
  place-items: center;

  h3{
    color:#fff;
  }
}

main{
  display:flex;
  width:100vw;

  .menu{
    display:flex;
    position: fixed;
    top:0;
    left:0;
    width:100%;
   
    button{
      display: flex;
      align-items:center;
      margin:0;
      background: transparent;
      
      border: none;
      border-radius: 5px;
      width:4rem;
      text-align: center;
      justify-content: center;
      padding:1rem .5rem;
      font-size:16px;
      cursor: pointer;
    
    
      svg{
        transform: scaleX(-1);

    }

      &.rotatemenu{
        animation:rotatemenu .3s ease-in-out forwards;
      }
      
    }
  }

  .sidebar{
    background:var(--chat-panel-background);
    background:#131719;
    width:20rem;
    height:100vh;
    display:flex;
    flex-direction: column;
    transition: .3s ease-in-out;
    

    

    .top-section{
      display:flex;
      width:100%;
      justify-content: flex-end;
      margin-top: 3rem;
      
      button{
        display: flex;
        align-items:center;
        margin:20px;
        background: #8147fc;
        color: white;
        border: none;
        border-radius: 5px;
        width:100%;
        text-align: center;
        justify-content: center;
        padding:.5rem;
        font-size:16px;
        
        cursor: pointer;
      }
      .menu{
        display:flex;
        position:static;
        justify-content: flex-end;
      }
    }

    .next-section{
      display:flex;
      padding:0;


      button{
        display: flex;
        align-items:center;
        margin:20px;
        background: #888;
        color: white;
        border: none;
        border-radius: 5px;
        width:100%;
        text-align: center;
        justify-content: center;
        padding:.5rem;
        font-size:16px;

        
        cursor: pointer;
      }
    }

    

    .conversations{
      color:#fff;
      margin:.5rem 1rem;
      height:100vh;
      max-height:calc(100vh - 150px);
      overflow-x: hidden;
      overflow-y: auto;
      position: relative;
      .conversation__item__details__last-message{
        padding:.5rem 1rem;
        width:100%;
        text-transform: capitalize;
        transition: all .3s ease;
        font-size: 14px;
        margin:0.2rem 0;
        
        &.active{
          color: rgb(129, 71, 252);
        }

        &:hover{
          color: #a3a3a3;
        }
      }

      
      
    }

  }
}


button.logout{
  width:fit-content;
  
  bottom:2rem;
  padding:.5rem 1rem;
  border-radius:.5rem;
  background:transparent;
  border:1px solid transparent !important;
  color:#fff;
  transition: all .3s ease;

  cursor: pointer;
  svg{
    fill:#f44335
  }

  &:hover{
    background:transparent;
    color:#F44335;
    border:1px solid #F44335 !important;
  }
   
}


@media screen and (max-width:768px) {
    .menu{
        display:flex;
    }
    main .sidebar{
        position: absolute;
        z-index:99;
        top:0;
        left:-20rem;
        width: 20rem;
        animation:slidein .3s ease-in-out forwards;
        

        &.closed{
            animation:slideout .3s ease-in-out forwards;

            
        }
    }
}


@keyframes rotatemenu {
    100%{
        transform: scaleX(-1);
    }
    
}

@keyframes slidein {
    
    100%{
        left: 0;
    }    
}
@keyframes slideout {
    
    100%{
        left: -20rem;
    }    
}




@keyframes fadein {
    100%{
        opacity: 1;
    }
}



@keyframes bounce {
    30% { transform: translateY(-2px); }
    60% { transform: translateY(0px); }
    80% { transform: translateY(2px); }
    100% { transform: translateY(0px); opacity: 0.5;  }
  }




#chat {
  background: var(--chat-background);
  
  box-sizing: border-box;
  padding: 2rem;
  border-top-right-radius: 12px;
  border-bottom-right-radius: 12px;
  position: relative;
  overflow: hidden;
  width:100%;
}
#chat::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url(../assets/screenshot.png) fixed;
  background-size:cover;
  z-index: -1;
}
#chat .btn-icon {
  position: relative;
  cursor: pointer;
}
#chat .btn-icon svg {
  stroke: #FFF;
  fill: #FFF;
  width: 50%;
  height: auto;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
#chat .chat__conversation-board {
  padding: 1em 0 2em;
  height: calc(100vh - 55px - 2em - 25px * 2 - .5em - 3em);
  overflow: auto;
}
#chat .chat__conversation-board__message-container.reversed {
  flex-direction: row-reverse;
}
#chat .chat__conversation-board__message-container.reversed .chat__conversation-board__message__bubble {
  position: relative;
}
#chat .chat__conversation-board__message-container.reversed .chat__conversation-board__message__bubble span:not(:last-child) {
  margin: 0 0 2em 0;
}
#chat .chat__conversation-board__message-container.reversed .chat__conversation-board__message__person {
  margin: 0 0 0 1.2em;
}
#chat .chat__conversation-board__message-container.reversed .chat__conversation-board__message__options {
  align-self: center;
  position: absolute;
  left: 0;
  display: none;
}
#chat .chat__conversation-board__message-container {
  position: relative;
  display: flex;
  flex-direction: row;
}
#chat .chat__conversation-board__message-container:hover .chat__conversation-board__message__options {
  display: flex;
  align-items: center;
}
#chat .chat__conversation-board__message-container:hover .option-item:not(:last-child) {
  margin: 0 0.5em 0 0;
}
#chat .chat__conversation-board__message-container:not(:last-child) {
  margin: 0 0 2em 0;
}
#chat .chat__conversation-board__message__person {
  text-align: center;
  margin: 0 1.2em 0 0;
}
#chat .chat__conversation-board__message__person__avatar {
  height: 35px;
  width: 35px;
  overflow: hidden;
  border-radius: 50%;
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
  ms-user-select: none;
  position: relative;
}
#chat .chat__conversation-board__message__person__avatar::before {
  content: "";
  position: absolute;
  height: 100%;
  width: 100%;
}
#chat .chat__conversation-board__message__person__avatar img {
  height: 100%;
  width: 100%;
  object-fit:cover;
}
#chat .chat__conversation-board__message__person__nickname {
  font-size: 9px;
  color: #484848;
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
  display: none;
}
#chat .chat__conversation-board__message__context {
  max-width: 55%;
  align-self: flex-end;
}
#chat .chat__conversation-board__message__options {
  align-self: center;
  position: absolute;
  right: 0;
  display: none;
}
#chat .chat__conversation-board__message__options .option-item {
  border: 0;
  background: 0;
  padding: 0;
  margin: 0;
  height: 16px;
  width: 16px;
  outline: none;
}
#chat .chat__conversation-board__message__options .emoji-button svg {
  stroke: var(--chat-options-svg);
  fill: transparent;
  width: 100%;
}
#chat .chat__conversation-board__message__options .more-button svg {
  stroke: var(--chat-options-svg);
  fill: transparent;
  width: 100%;
}
#chat .chat__conversation-board__message__bubble span {
  width: -webkit-fit-content;
  width: -moz-fit-content;
  width: fit-content;
  display: inline-table;
  word-wrap: break-word;
  background: var(--chat-bubble-background);
  font-size: 13px;
  color: var(--chat-text-color);
  padding: 0.5em 0.8em;
  line-height: 1.5;
  border-radius: 6px;
  font-family: "Lato", sans-serif;
}
#chat .chat__conversation-board__message__bubble:not(:last-child) {
  margin: 0 0 0.3em;
}
#chat .chat__conversation-board__message__bubble:active {
  background: var(--chat-bubble-active-background);
}
#chat .chat__conversation-panel {
  background: var(--chat-panel-background);
  border-radius: 12px;
  padding: 0 1em;
  height: 55px;
  margin: 0.5em 0 0;
  
}
#chat .chat__conversation-panel__container {
  display: flex;
  flex-direction: row;
  align-items: center;
  height: 100%;
}
#chat .chat__conversation-panel__container .panel-item:not(:last-child) {
  margin: 0 1em 0 0;
}
#chat .chat__conversation-panel__button {
  background: grey;
  height: 20px;
  width: 30px;
  border: 0;
  padding: 0;
  outline: none;
  cursor: pointer;
}
#chat .chat__conversation-panel .add-file-button {
  height: 23px;
  min-width: 23px;
  width: 23px;
  background: var(--chat-add-button-background);
  border-radius: 50%;
}
#chat .chat__conversation-panel .add-file-button svg {
  width: 100%;
  fill:#8417fc;
  stroke: #54575c;
}
#chat .chat__conversation-panel .emoji-button {
  min-width: 23px;
  width: 23px;
  height: 23px;
  background: transparent;
  border-radius: 50%;
}
#chat .chat__conversation-panel .emoji-button svg {
  width: 100%;
  fill: transparent;
  stroke: #54575c;
}
#chat .chat__conversation-panel .send-message-button {
  background: var(--chat-send-button-background);
  height: 36px;
  min-width: 36px;
  border-radius: 50%;
  transition: 0.3s ease;
}
#chat .chat__conversation-panel .send-message-button:active {
  transform: scale(0.97);
}
#chat .chat__conversation-panel .send-message-button svg {
  margin: 1px -1px;
}
#chat .chat__conversation-panel__input {
  width: 100%;
  height: 100%;
  outline: none;
  position: relative;
  color: var(--chat-text-color);
  font-size: 13px;
  background: transparent;
  border: 0;
  font-family: "Lato", sans-serif;
  resize: none;
}





@media only screen and (max-width: 600px) {
  #chat {
    margin: 0;
    border-radius: 0;
    padding:0;
  }
  #chat .chat__conversation-board {
    height: calc(100vh - 55px - 2em - .5em - 3em);
  }
  #chat .chat__conversation-board__message__options {
    display: none !important;
  }
}

.typing{
  .chat__conversation-board__message__bubble {
      opacity:0;
      background: rgba(10, 14, 14, 0.45);
      padding: 8px 13px 9px 13px;
      position: relative;
  display: inline-block;
  margin-bottom: 5px;
  color: #fff;
  font-size: 0.7rem;
  padding: 10px 10px 10px 12px;
  border-radius: 20px;
  animation:fadein .3s ease forwards;
    }
  .ellipsis {
      width: 10px;
      height: 10px;
      display: inline-block;
      background: rgba(10, 14, 14, 0.25);
      border-radius: 50%;
      margin:0 .2rem;
      animation: bounce 1.3s linear infinite;

      
  }
  
  .one {
      animation-delay: 0.6s;
  }
  .two {
      animation-delay: 0.5s;
  }
  .three {
      animation-delay: 0.8s;
  }

}

</style>
