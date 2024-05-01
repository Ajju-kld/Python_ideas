const axios = require("axios");

const API_ENDPOINT = "https://api.140.ieeer10.org/api/activity/list";
const NUM_USERS = 1000000;

async function sendRequest() {
  console.log("Sending request to:", API_ENDPOINT);
  try {
    const response = await axios.get(API_ENDPOINT);
    if (response.status === 200) {
      console.log("Request sent and received successfully.");
    } else {
      console.error("Error: Unexpected response status:", response.status);
    }
  } catch (error) {
    console.error("Error sending request:", error.message);
  }
}

async function simulateUsers() {
  const promises = [];
  for (let i = 0; i < NUM_USERS; i++) {
    promises.push(sendRequest());
  }
  await Promise.all(promises);
}

simulateUsers()
  .then(() => {
    console.log("All requests sent.");
  })
  .catch((error) => {
    console.error("Error simulating users:", error);
  });
