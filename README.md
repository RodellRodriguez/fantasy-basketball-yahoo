## fantasy-basketball-yahoo

**Description**

It is my first time playing Fantasy Basketball and my friends decided to use Yahoo's Fantasy Basketball website. The NBA has 82 games in the season so that means I would need to choose which of my players to start at least 82 times. I decided to create a Python script, utilizing the Selenium library, that automates the task of starting your active players for as many days as the user desires. Active means a player is playing on the corresponding date. Additionally, if an active player ends up on the bench, the user will get notified with the date and player that this situation applies to. This safety measure is so that the user can look into this matter and decide for himself/herself who to start and who to bench.

The default number of days that the script will automate is set to 7 days. Feel free to change the number as you see fit.

**Dependencies**
* Python 3.5
* Selenium WebDriver
* [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads). Additionally check out their ["Getting stated"](https://sites.google.com/a/chromium.org/chromedriver/getting-started) page 

**Setup**
1. Download script
2. Change any of the capitilized variables in the script as necessary e.g. YAHOO_EMAIL, YAHOO_PASSWORD, and CHROME_DRIVER_PATH for the location of your chromedriver.exe file.
3. Change NUM_OF_PLAYERS variable to 14 if you are allowed to have an extra player on your roster if one of your players is injured
4. Install dependencies
5. Run Program

**To-Do List**

- [ ] Exception handling
- [x] Do a report for x number of days
- [x] Have the report mention if any benched players are Active
- [ ] Account for fantasy rule where you can have an additional player on your roster if one of your players is injured
- [ ] Report status of a player e.g. Healthy, Injured, Out, Game Time Decision(GTD)