import kue from "kue";

// Create a queue
const queue = kue.createQueue();

// Blacklisted phone numbers
const blacklist = ["4153518780", "4153518781"];

// Function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  // Track initial progress
  job.progress(0, 100);

  // Check if phone number is blacklisted
  if (blacklist.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Simulate sending notification
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  
  // Mark job as completed
  done();
}

// Process jobs from the queue
queue.process("push_notification_code_2", 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
