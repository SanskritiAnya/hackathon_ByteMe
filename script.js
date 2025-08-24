const API_BASE_URL = "http://10.1.40.87:8000";  // replace with your backend IP and port

import { getChatbotResponse } from './features/mentalHealthSupport.js';

document.addEventListener('DOMContentLoaded', () => {
  const currentPage = window.location.pathname.split('/').pop();

  // 🔐 LOGIN PAGE: Handle form submission
  const loginForm = document.getElementById('loginForm');
  if (loginForm) {
    loginForm.addEventListener('submit', function (e) {
      e.preventDefault();

      const parentName = document.getElementById('parentName').value.trim();
      const childName = document.getElementById('childName').value.trim();
      const parentEmail = document.getElementById('parentEmail').value.trim();
      const parentDOB = document.getElementById('parentDOB').value;
      const childDOB = document.getElementById('childDOB').value;
      const disability = document.getElementById('disability').value;
      const notes = document.getElementById('notes').value.trim();
      const profilePicFile = document.getElementById('profilePic').files[0];

      if (!parentName || !childName) {
        alert('Please enter both names.');
        return;
      }

      localStorage.setItem('parentName', parentName);
      localStorage.setItem('childName', childName);
      localStorage.setItem('parentEmail', parentEmail);
      localStorage.setItem('parentDOB', parentDOB);
      localStorage.setItem('childDOB', childDOB);
      localStorage.setItem('disability', disability);
      localStorage.setItem('notes', notes);

      if (profilePicFile) {
        const reader = new FileReader();
        reader.onload = function () {
          localStorage.setItem('profilePic', reader.result);
          window.location.href = 'index.html';
        };
        reader.readAsDataURL(profilePicFile);
      } else {
        window.location.href = 'index.html';
      }
    });
  }

  // 🔍 Check login status
  const parentName = localStorage.getItem('parentName');
  const childName = localStorage.getItem('childName');
  const disability = localStorage.getItem('disability');
  const savedPic = localStorage.getItem('profilePic');

  if ((!parentName || !childName) && currentPage !== 'login.html') {
    window.location.href = 'login.html';
    return;
  }

  // 🧑‍💻 Populate sidebar and dashboard
  const sidebarName = document.getElementById('sidebarName');
  const sidebarChild = document.getElementById('sidebarChild');
  const welcomeMessage = document.getElementById('welcomeMessage');
  const parentSummary = document.getElementById('parentSummary');
  const childSummary = document.getElementById('childSummary');
  const disabilitySummary = document.getElementById('disabilitySummary');
  const profileImage = document.getElementById('profileImage');

  if (sidebarName) sidebarName.textContent = parentName || 'Parent';
  if (sidebarChild) sidebarChild.textContent = `Parent of ${childName || 'Child'}`;
  if (welcomeMessage) welcomeMessage.textContent = `Welcome, ${parentName || 'Parent'}!`;
  if (parentSummary) parentSummary.textContent = parentName || 'N/A';
  if (childSummary) childSummary.textContent = childName || 'N/A';
  if (disabilitySummary) disabilitySummary.textContent = disability || 'N/A';
  if (profileImage && savedPic) profileImage.src = savedPic;

  // 🔗 Highlight active navigation link
  const navLinks = document.querySelectorAll('nav a');
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });

  // 💬 MENTAL HEALTH CHATBOT
  const chatInput = document.getElementById('chatInput');
  const chatMessages = document.getElementById('chatMessages');

  if (chatInput && chatMessages) {
    window.sendChat = function () {
      const message = chatInput.value.trim();
      if (!message) return;

      const userMsg = `<div class="chat-message user">🧍 You: ${message}</div>`;
      chatMessages.innerHTML += userMsg;

      const reply = getChatbotResponse(message);
      const botMsg = `<div class="chat-message bot">🤖 Copilot: ${reply}</div>`;
      chatMessages.innerHTML += botMsg;

      chatInput.value = '';
      chatMessages.scrollTop = chatMessages.scrollHeight;
    };
  }
});






async function fetchNearbyResources(resourceType, latitude, longitude, radiusKm = 5) {
  const url = `${API_BASE_URL}/emergency?resource_type=${encodeURIComponent(resourceType)}&latitude=${latitude}&longitude=${longitude}&radius_km=${radiusKm}`;

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error('Network response was not OK');
    }
    const data = await response.json();
    console.log('Nearby resources:', data);
    return data;
  } catch (error) {
    console.error('Error fetching nearby resources:', error);
    return null;
  }
}








function getUserLocationAndFetchResources() {
  if (!navigator.geolocation) {
    alert('Geolocation is not supported by your browser');
    return;
  }

  navigator.geolocation.getCurrentPosition(
    async (position) => {
      const lat = position.coords.latitude;
      const lon = position.coords.longitude;
      console.log('User location:', lat, lon);

      // Example: Fetch ambulances nearby
      const ambulances = await fetchNearbyResources('ambulance', lat, lon);

      if (ambulances && ambulances.length > 0) {
        // TODO: Render ambulances on UI or map
        console.log('Ambulances nearby:', ambulances);
      } else {
        console.log('No ambulances found nearby.');
      }
    },
    (error) => {
      console.error('Error getting location:', error);
      alert('Unable to retrieve your location');
    }
  );
}




window.onload = () => {
  getUserLocationAndFetchResources();
};





/**
 * @license
 * Copyright 2019 Google LLC. All Rights Reserved.
 * SPDX-License-Identifier: Apache-2.0
 */
let map;

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");

  map = new Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
}
