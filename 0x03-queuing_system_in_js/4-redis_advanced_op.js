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

// storing a hash on multiple fields using hset
const createHash = () => {
  client.hset('HolbertonSchools', 'Portland', 50, (err, resp) => {
    if (err) {
      console.log('Error setting Portland: ', err);
    } else {
      console.log('Reply: ', resp);
    }
  });
  client.hset('HolbertonSchools', 'Seattle', 80, (err, resp) => {
    if (err) {
      console.log('Error setting Seattle: ', err);
    } else {
      console.log('Reply: ', resp);
    }
  });
  client.hset('HolbertonSchools', 'New York', 20, (err, resp) => {
    if (err) {
      console.log('Error setting New York: ', err);
    } else {
      console.log('Reply: ', resp);
    }
  });
  client.hset('HolbertonSchools', 'Bogota', 20, (err, resp) => {
    if (err) {
      console.log('Error setting Bogota: ', err);
    } else {
      console.log('Reply: ', resp);
    }
  });
  client.hset('HolbertonSchools', 'Cali', 40, (err, resp) => {
    if (err) {
      console.log('Error setting Cali');
    } else {
      console.log('Reply: ', resp);
    }
  });
  client.hset('HolbertonSchools', 'Paris', 2, (err, resp) => {
    if (err) {
      console.log('Error setting Paris');
    } else {
      console.log('Reply: ', resp);
    }
  });
}

// Displaying the hash content
const displayHash = () => {
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.log('Error fetching the hash: ', err);
    } else {
      console.log(reply);
    }
  });
};

// Running the operations
createHash();
displayHash();
