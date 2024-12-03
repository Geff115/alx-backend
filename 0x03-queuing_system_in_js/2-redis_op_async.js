// I did not use redis.print due to the higher version of Redis server
// I am running on my machine. I instead used a callback function.

import { redisClientFactory } from "kue";
import { createClient } from "redis";
import { promisify } from "util";

// Initializing a redis client
const client = createClient();

// Promisifying the Redis get and set methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Connect event listener
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Error event listener
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Async function to set a new school value
async function setNewSchool (schoolName, value) {
    try {
      const reply = await setAsync(schoolName, value);
      console.log(`Reply: ${reply}`);
    } catch (err) {
      console.log(`Error setting ${schoolName}: ${err.message}`);
    }
}


async function displaySchoolValue (schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(`${reply}`);
  } catch (err) {
    console.log(`Error fetching value for ${schoolName}: ${err.message}`);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
