const fs = require("fs");
const express = require("express");
const app = express();

// Load dataset
const dataset = JSON.parse(fs.readFileSync("dataset.json", "utf-8"));

// Keep track of current index
let currentIndex = 0;

app.get("/api/gold", (req, res) => {
  // Get current item
  const item = dataset[currentIndex];

  // Send it as JSON
  res.set("Content-Type", "application/json");
  res.status(200).send(item);

  // Move to next index
  currentIndex++;

  // Wrap around if end is reached
  if (currentIndex >= dataset.length) {
    currentIndex = 0;
  }
});

app.listen(3000, () => {
  console.log("Gold Data Server running on http://localhost:3000");
});