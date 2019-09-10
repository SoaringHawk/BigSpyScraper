# BigSpyScraper
Ecommerce website Scraper 
'''
This scraper uses selenium webdriver to create an instance of the browser to scrape data from the targeted website.
Selenium can be used with any browser (Chrome, Firefox...), but this bot uses Chomedriver which is provided within this repository, however chromedriver has to be installed on your computer for this to work, just google chromedriver or driver for any browser used and download it.
Also take a look at the requirements file to know the proper package to install.

Selenium use a live representation within the browser which displays the process, this is effective in order to scrape data from site that could require Capchat in which case the user can take over and solve this as fast as possible.

Everything is configured, an account has been created, the login info can be found in the config file if needed.

Run the script from the scraper file, everything is automated until the login process where the user will need to click on the capchat button and solve it within 150 second sleeptime implemented in the bot, then click on the login button and wait until the bot automatically takeover and redirect once the sleeptime over (Note that the time required in order to solve the capchat varies and the waittime can be modified in the script in the login section where it is commented ##login## and waittime).

Once the login process completed the bot start to scrape data from the site, by default the json data in printed everytime a page is completed, this can be modified by commenting the print statement in the script.

#When the process is over all the json data will be included in the bulk_json_data variable, so it might be inconvenient to print it out# 
