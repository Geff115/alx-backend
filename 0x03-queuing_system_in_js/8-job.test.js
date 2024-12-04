import { expect } from 'chai';
import { createQueue } from 'kue';
import createPushNotificationsJobs from '../8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = createQueue(); // Initialize Kue queue
    queue.testMode.enter(); // Enter test mode to simulate jobs
  });

  afterEach(() => {
    queue.testMode.clear(); // Clear the queue
    queue.testMode.exit(); // Exit test mode
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(42, queue)).to.throw('Jobs is not an array');
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('should create jobs in the queue when given a valid jobs array', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'This is a test message 1' },
      { phoneNumber: '0987654321', message: 'This is a test message 2' },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2); // Verify the number of jobs created
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3'); // Verify job type
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]); // Verify first job data
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]); // Verify second job data
  });

  it('should properly handle job events', (done) => {
    const jobs = [{ phoneNumber: '1234567890', message: 'Test message' }];
    const queue = createQueue(); // Create a new queue instance

    const job = queue.create('push_notification_code_3', jobs[0]);

    // Add event listeners
    job
      .on('enqueue', () => {
        expect(job.id).to.be.a('number');
      })
      .on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
        done(); // Complete the test
      })
      .on('failed', (err) => {
        expect.fail(`Job failed with error: ${err.message}`);
        done(); // Fail the test if it reaches here
      });

    job.save(); // Save the job to trigger event listeners
    done();
  });
});
