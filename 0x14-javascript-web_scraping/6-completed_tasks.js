#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

const url = process.argv[2];

// Fetch data from the API URL
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  // Parse the JSON response
  const todos = JSON.parse(body);

  // Initialize an object to hold the count of completed tasks per user
  const completedTasksCount = {};

  // Process each task
  todos.forEach(task => {
    if (task.completed) {
      const userId = task.userId;
      if (!completedTasksCount[userId]) {
        completedTasksCount[userId] = 0;
      }
      completedTasksCount[userId]++;
    }
  });

  // Print out the number of completed tasks for each user ID
  console.log(completedTasksCount);
});
