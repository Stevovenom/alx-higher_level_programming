#0x14. JavaScript - Web scraping

<a href="https://serpapi.com/blog/web-scraping-in-javascript-complete-tutorial-for-beginner/">Web scraping with javascript</a><br>

#JavaScript Web Scraping: Detailed Explanation with Examples

<strong>Web scraping involves extracting data from websites.</strong> JavaScript can be used for web scraping, particularly with Node.js, leveraging libraries like <i><strong>axios, cheerio, and puppeteer</strong></i>.<br></br> Here’s a detailed guide to understanding and performing web scraping using JavaScript:

1. Key Concepts<br>
<u>HTTP Requests:</u> To scrape a website, you first need to fetch the HTML content. This is done by making HTTP requests to the target website.
<br>
<u>Parsing HTML:</u> Once you have the HTML content, you need to parse it to extract the required data.
<br>
<u>Handling Dynamic Content:</u> Some websites load content dynamically using JavaScript. This requires more advanced techniques like headless browser automation.

2. Essential Libraries<br>
<strong>axios:</strong> A promise-based HTTP client for making requests.<br>
<strong>cheerio:</strong> A fast, flexible, and lean implementation of core jQuery designed specifically for the server.<br>
<strong>puppeteer:</strong> A Node library providing a high-level API to control Chrome or Chromium over the DevTools Protocol.<br>

Basic Example: <strong>Scraping Static Websites</strong><br>
Let's start with a simple example of scraping a static website using axios and cheerio.

#Step 1: Setting Up
First, create a new Node.js project and install the necessary libraries:
<code>
# create a directory
mkdir web-scraping
cd web-scraping
npm init -y
npm install axios cheerio
</code><br>

#Step 2: Writing the Script
Create a file named scrape.js:

<code>
const axios = require('axios');
const cheerio = require('cheerio');

// URL of the page we want to scrape
const url = 'https://example.com';

axios.get(url)
    .then(response => {
        const html = response.data;
        const $ = cheerio.load(html);

        // Example: Extract the title of the page
        const title = $('title').text();
        console.log('Title:', title);

        // Example: Extract all links
        $('a').each((index, element) => {
            const link = $(element).attr('href');
            console.log(link);
        });
    })
    .catch(error => {
        console.error('Error fetching the URL:', error);
    });

</code><br>

<strong>In this script:</strong>

1. We use axios to fetch the HTML content of the webpage.
2. We load the HTML content into cheerio to parse and manipulate the DOM.
3. We extract and print the page title and all the links (<a> elements) on the page.<br>


Advanced Example:<strong> Scraping Dynamic Websites</strong><br>
For websites that load content dynamically with JavaScript, we need to use a headless browser like <strong>Puppeteer</strong>.
<br>

#Step 1: Setting Up Puppeteer
1. Install Puppeteer:
<code>
npm install puppeteer
</code><br>

#Step 2: Writing the Script
2. Create a file named scrape_dynamic.js:

<code>
const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    // URL of the dynamic page we want to scrape
    const url = 'https://example.com';

    await page.goto(url, { waitUntil: 'networkidle2' });

    // Example: Extract the title of the page
    const title = await page.evaluate(() => document.title);
    console.log('Title:', title);

    // Example: Extract all links
    const links = await page.evaluate(() => {
        return Array.from(document.querySelectorAll('a')).map(link => link.href);
    });
    console.log(links);

    await browser.close();
})();

</code>

<br>

In this script:

1. We use Puppeteer to launch a headless browser and open a new page.
2. We navigate to the target URL and wait until the network is idle.
3. We use page.evaluate to run JavaScript in the context of the page to extract the page title and all links.
4. We close the browser.<br></br>


#Practical Applications
1. Price Monitoring: Scraping e-commerce websites to monitor price changes.
2. Data Aggregation: Collecting data from multiple sources for analysis or presentation.
3. Competitor Analysis: Keeping track of competitor websites for new product releases, pricing, etc.
4. Content Extraction: Extracting articles, news, or other content from websites for aggregation or personal use.
<br>

#Legal and Ethical Considerations
While web scraping is a powerful tool, it is essential to consider the legal and ethical implications.<br>

By understanding these concepts and using the appropriate tools and techniques, you can effectively scrape data from both static and dynamic websites using JavaScript.<br>

#Further Reading
<a href="https://intranet.alxswe.com/rltoken/ONv-sSv-FA87Mc5rMZmO6A">Working with JSON data</a>
<a href="https://intranet.alxswe.com/rltoken/zm0h7FqpQCZZpPZqxxwLxA">The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco</a>
<a href="https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ">Request Module</a>
<a href="https://intranet.alxswe.com/rltoken/j2PStAUtVPdXKwrrFxpt0g">Modern JS</a>
<a href="https://pptr.dev/">Puppeteer Documentation</a>
<a href="https://axios-http.com/">Axios Documentation</a>
<a href="https://github.com/Stevovenom/modern-js-cheatsheet">Modern JS cheetcode</a>
