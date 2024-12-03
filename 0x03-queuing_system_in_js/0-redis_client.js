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
