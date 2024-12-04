import { createClient } from "redis";

const client = createClient();

// Event listeners
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Subscribing to the channel
const channel = "holberton school channel";
client.subscribe(channel, () => {
  console.log(`Subscribed to channel: ${channel}`);
});

client.on('message', (channel, message) => {
  console.log(`Received message: ${message}`);
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    client.quit();
  }
});
