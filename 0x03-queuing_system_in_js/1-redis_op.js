// I did not use redis.print due to the higher version of Redis server
// I am running on my machine. I instead used a callback function.

import { redisClientFactory } from "kue";
import { createClient } from "redis";

// Initializing a redis client
const client = createClient();

// Connect event listener
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Error event listener
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Setting a new school value
function setNewSchool (schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.log(`Error setting ${schoolName}: ${err.message}`);
    } else {
      console.log(`Reply: ${reply}`);
    }
  });
}

function displaySchoolValue (schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.log(`Error fetching value for ${schoolName}: ${err.message}`);
    } else {
      console.log(`${reply}`);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
