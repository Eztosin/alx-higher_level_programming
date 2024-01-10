#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Please provide the API URL as an argument.');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    if (response.statusCode === 200) {
      const todos = JSON.parse(body);
      const completedTasks = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          if (completedTasks[todo.userId]) {
            completedTasks[todo.userId]++;
          } else {
            completedTasks[todo.userId] = 1;
          }
        }
      });

      console.log(completedTasks);
    } else {
      console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
    }
  }
});
