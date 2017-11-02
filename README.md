## fantasy-basketball-yahoo

**Description**

It is my first time playing Fantasy Basketball and my friends decided to use Yahoo's Fantasy Basketball website. The NBA has 82 games in the season so that means I would need to choose which of my players to start at least 82 times. I decided to create a Python script, utilizing the Selenium library, that automates the task of starting your active players for as many days as the user desires by clicking the "Start Active Players" button on the Yahoo Fantasy UI. Active means a player's team is playing on the corresponding date.

4 cases where the report will tell the user to investigate their roster:
1. When an active player is on the bench. This will only occur if more than 10 players are active for that day.
2. When an active player's status is Injured
3. When an active player's status is Out
4. When an active player's status is GTD

If any of these 4 situations occur, then it is in the user's best interest to manually set up their roster for that day.

Note:
1. The default number of days that the script will automate is set to 7 days. Feel free to change the number in the source code as the user sees fit.
2. This script assumes the user is only enrolled in ONE Yahoo Fantasy League. I have not accounted for multiple leagues
3. This script assumes the user has 13 players. I have not accounted for 14 players if the user has an injured player

**Dependencies**
* Python 3.5
* Selenium WebDriver
* [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads). Additionally check out their ["Getting started"](https://sites.google.com/a/chromium.org/chromedriver/getting-started) page 

**Setup**
1. Download script
2. Install dependencies
3. Change CHROME_DRIVER_PATH to the location of your chromedriver.exe file if necessary.
4. Change NUM_OF_PLAYERS variable if necessary
5. Run Program

**To-Do List**

- [x] Capability of creating a report for x number of days
- [x] Report status of a player e.g. Healthy, Injured, Out, Game Time Decision(GTD)
- [x] Have the report mention if any Benched, Injured, Out, and GTD players are Active
- [x] Have the script prompt the user for their yahoo email, password, and team name instead of editing the source code
- [ ] Account for fantasy rule where you can have an additional player on your roster if one of your players is injured
- [ ] Exception handling
- [ ] Remove print statements and implement logging practices
- [ ] Implement Page Object Model to practice code maintainability and loose coupling coding practices