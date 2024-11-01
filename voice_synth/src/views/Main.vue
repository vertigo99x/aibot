<template>
    <main>
      
        <div class="sidebar" :class="{'closed':!isSidebarOpen}">
            <div class="menu">
                <button @click="isSidebarOpen = !isSidebarOpen" :class="{'rotatemenu':!isSidebarOpen}"><svg xmlns="http://www.w3.org/2000/svg" height="36px" viewBox="0 -960 960 960" width="24px" fill="#F44335"><path d="M360-120v-720h80v720h-80Zm160-160v-400l200 200-200 200Z"/></svg></button>
                </div>
          <div class="top-section" v-if="isSidebarOpen || isBig()">
            
            <button style="padding:.5rem"><span >New Conversation</span>
              <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M440-440H200v-80h240v-240h80v240h240v80H520v240h-80v-240Z"/></svg></button>
          </div>
          <div class="conversations">
            <div class="conversation__item">
              <div class="conversation__item__details">
                <div class="conversation__item__details__last-message">Convo</div>
              </div>
            </div>
            <div class="conversation__item">
              <div class="conversation__item__details">
                <div class="conversation__item__details__last-message">Convo</div>
              </div>
            </div>
            <div class="conversation__item">
              <div class="conversation__item__details">
                <div class="conversation__item__details__last-message">Convo</div>
              </div>
            </div>
          </div>
        </div>
        <div class="--dark-theme" id="chat">
            <div class="menu">
                <button @click="isSidebarOpen = !isSidebarOpen" :class="{'rotatemenu':!isSidebarOpen}"><svg xmlns="http://www.w3.org/2000/svg" height="36px" viewBox="0 -960 960 960" width="24px" fill="#F44335"><path d="M360-120v-720h80v720h-80Zm160-160v-400l200 200-200 200Z"/></svg></button>
                </div>
          <div class="chat__conversation-board">
            
            <div class="chat__conversation-board__message-container" v-for="item in conversation" :key="item" :class="{'reversed':item.isUser}">
              <div class="chat__conversation-board__message__person">
                <div class="chat__conversation-board__message__person__avatar"><img src="https://randomuser.me/api/portraits/men/32.jpg" alt="Thomas Rogh"/></div><span class="chat__conversation-board__message__person__nickname">AI Buddy</span>
              </div>
              <div class="chat__conversation-board__message__context">
                <div class="chat__conversation-board__message__bubble"> <span>{{item.text}}</span></div>
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

           
            <div class="chat__conversation-board__message-container typing" v-if="isLoading">
              <div class="chat__conversation-board__message__person">
                <div class="chat__conversation-board__message__person__avatar"><img src="https://randomuser.me/api/portraits/men/9.jpg" alt="Dennis Mikle"/></div><span class="chat__conversation-board__message__person__nickname">Dennis Mikle</span>
              </div>
              <div class="chat__conversation-board__message__context">
                <div class="chat__conversation-board__message__bubble">
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
              <button class="chat__conversation-panel__button panel-item btn-icon add-file-button">
                <svg class="feather feather-plus sc-dnqmqq jxshSx" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                  <line x1="12" y1="5" x2="12" y2="19"></line>
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                </svg>
              </button>
              
              <input class="chat__conversation-panel__input panel-item" placeholder="Type a message..." v-model="searchText">
              <button class="chat__conversation-panel__button panel-item btn-icon send-message-button" style="background:#4CAF50;" @click="toggleListening()">
                
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M480-400q-50 0-85-35t-35-85v-240q0-50 35-85t85-35q50 0 85 35t35 85v240q0 50-35 85t-85 35Zm0-240Zm-40 520v-123q-104-14-172-93t-68-184h80q0 83 58.5 141.5T480-320q83 0 141.5-58.5T680-520h80q0 105-68 184t-172 93v123h-80Zm40-360q17 0 28.5-11.5T520-520v-240q0-17-11.5-28.5T480-800q-17 0-28.5 11.5T440-760v240q0 17 11.5 28.5T480-480Z"/></svg>
              </button>
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
              <img :src="animation" alt="">
              <p>{{transcription}}</p>
            </div>
          </div>
        </div>
       </main>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue';
import animation from '../assets/animation.gif'; 
import axios from 'axios'
import { useStore } from 'vuex';
import { useRouter, useRoute } from 'vue-router';

const store = useStore();
const isListening = ref(false);
const isLoading = ref(false);
const router = useRouter();
const conversation = ref(store.getters.conversation);
const $http = inject('$http');
const searchText = ref('');
const transcription = ref(''); 
const isSidebarOpen = ref(false);
let recognition;


onMounted(() => {

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


const isBig = () => {
    return window.innerWidth > 768;
}

const toggleListening = () => {
  if (isListening.value) {
    recognition.stop();
    isListening.value = false;
  } else {
    transcription.value = '';
    isListening.value = true;
    recognition.start();
  }
};


const sendTextToApi = async (text) => {
    searchText.value = '';
    conversation.value.push({
      text: text,
      isUser: true,
    });
    store.commit('setConversation', conversation.value);
    isLoading.value = true;
    
  try {
    const data = {
      text:text,
    }
    const response = await $http.post('api/v1/getResponse', data);
    console.log(response.data)
    isLoading.value=false;
    conversation.value.push({
      text: response.data.response,
      isUser: false,
    });
    store.commit('setConversation', conversation.value);
    
    
  } catch (error) {
    console.error('Error fetching API:', error);
  }
};
</script>

<style lang="scss" scoped>



.--dark-theme {
  --chat-background: rgba(10, 14, 14, 0.95);
  --chat-panel-background: #131719;
  --chat-bubble-background: #14181a;
  --chat-add-button-background: #212324;
  --chat-send-button-background: #8147fc;
  --chat-text-color: #a3a3a3;
  --chat-options-svg: #a3a3a3;
}

body {
  background: url(https://images.unsplash.com/photo-1495808985667-ba4ce2ef31b3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80);
  background-size: cover;
  margin:0;
  padding:0;
}

main{
  display:flex;
  width:100vw;

  .menu{
    display:none;
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
        display:none;
        position:static;
        justify-content: flex-end;
      }
    }

    

    .conversations{
      color:#fff;
      margin:.5rem .1rem;
      .conversation__item__details__last-message{
        padding:.5rem;
        width:100%;
        text-transform: capitalize;
        transition: all .3s ease;
        font-size: 16px;

        &:hover{
          background: rgba(129, 71, 252, 0.5);
        }
      }
    }

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

.typing{
    .chat__conversation-board__message__bubble {
        opacity:0;
        background: lighten(#000, 45%);
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
        background: lighten(#000, 25%);
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
  background: url(https://images.unsplash.com/photo-1495808985667-ba4ce2ef31b3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80) fixed;
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
  width: auto;
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
  width: 70%;
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
  }
  #chat .chat__conversation-board {
    height: calc(100vh - 55px - 2em - .5em - 3em);
  }
  #chat .chat__conversation-board__message__options {
    display: none !important;
  }
}
</style>
