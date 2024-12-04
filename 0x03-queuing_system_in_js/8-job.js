import { createQueue } from "kue";

// Creating a queue
const queue = createQueue();

function createPushNotificationsJobs (jobs, queue) {
    // Ensuring the input is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Iterating through the job data and create jobs
  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData);

    job
      .on('enqueue', () => {
        console.log(`Notification job created: #${job.id}`);
      })
      .on('complete', () => {
        console.log(`Notification job #${job.id} completed`);
      })
      .on('failed', (err) => {
        console.log(`Notification job #${job.id} failed`);
      })
      .on('progress', (progress) => {
        console.log(`Notification job #${job.id} ${progress}% complete`);
      })

      // Saving the job to the queue
      job.save();
  });
}

export default createPushNotificationsJobs;
