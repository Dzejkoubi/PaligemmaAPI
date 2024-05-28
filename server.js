const fs = require("fs");
const path = require("path");
const express = require("express");
const puppeteer = require("puppeteer");

const app = express();
const port = 3000;

app.use(express.static("public"));

app.get("/screenshot", async (req, res) => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(`http://localhost:${port}`);
  const screenshotPath = path.join(__dirname, "images", "screenshot.png");
  await page.screenshot({ path: screenshotPath });
  await browser.close();
  res.send("Screenshot saved!");
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
