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
2. Change any of the capitilized variables in the script e.g. username, password, team name, and chromedriver location depending on your OS
3. Install dependencies
4. Run Program

**To-Do List**

- [ ] Exception handling
- [x] Do a report for x number of days
- [x] Have the report mention if any benched players are Active