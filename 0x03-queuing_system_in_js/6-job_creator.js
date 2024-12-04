import kue from "kue";

// Create a queue
const queue = kue.createQueue();

// Job data
const jobData = {
  phoneNumber: "1234567890",
  message: "This is a push notification test",
};

// Create a job in the 'push_notification_code' queue
const job = queue.create("push_notification_code", jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.error(`Error creating job: ${err.message}`);
    }
  });

  // Event listener for job completion and failure
  job.on("complete", () => {
    console.log("Notification job is completed");
  });

  job.on("failed", () => {
    console.log("Notification job failed");
  });
  