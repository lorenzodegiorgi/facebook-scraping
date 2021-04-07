<!-- PROJECT LOGO -->
<br />


  <h3 align="center">Facebook Likes Scraper</h3>

  <p align="center">
  A simple and messy Python script that scrapes likes of the posts
  </p>
</p>



<!-- TABLE OF CONTENTS -->

<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

A simple and messy Python script that scrapes likes of the posts and save them in a CSV file
It has been built by using:

- BeautifulSoup and Selenium: for scraping the likes

The script MUST BE used only for didactical purpose since scraping activities violate Facebook's Community Standards (https://www.facebook.com/communitystandards/)

<!-- GETTING STARTED -->



## Getting Started

### Prerequisites

For working, the script needs the Chromedriver that must be place in the same folder of the script. 
Chromedriver can be found here:

https://chromedriver.chromium.org

Be sure that the version of Chromedriver is the same one of your Chrome application. 

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/lorenzodegiorgi/facebook-scraping
   ```
   
2. Install libraries
   ```sh
   pip install selenium
   pip install beautifulsoup4
   ```
   
3. Fill in a file called "links.txt" with the a line for each post's link to scrape such as:

   ```
   https://m.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=XXXXX
   ```

<!-- USAGE EXAMPLES -->



## Usage

Run the script for the first time and log in into your Facebook account in order to generate cookies

```sh
python3 facebookscraper.py
```

After that, close Google Chrome and re-run the script. 

Feel free to change the values of the configuration variables:

```
# CONFIGURATION VARIABLES
LIMIT = 400 # Number of likers in each page
LOADING_PAGE_TIME = 8 # Waiting time to load the new page
MIN_WAITING_TIME = 5 # Min waiting time to load the next page
MAX_WAITING_TIME = 10 # Max waiting time to load the next page
ERROR_WAITING = 10 #Time to wait before a new attempt
```

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.


