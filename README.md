# Yahoo Fantasy Basketball Start Your Players Automation

## Table of Contents

**[Description](#description)**<br>
**[Dependencies](#dependencies)**<br>
**[Setup](#setup)**<br>
**[Example Output](#example-output)**<br>
**[To-Do List](#to-do-list)**<br>

## Description

I am an avid basketball fan but never really got into the fantasy sports culture. It is my first time playing Fantasy Basketball and my friends decided to use Yahoo's Fantasy Basketball website to play. The NBA has 82 games in the season so that means I would need to choose which of my players to start at least 82 times. 

Seeing that it would be extremely tedious to constantly manually start my players I decided to create a Python script, utilizing the Selenium library, that automates the task of starting your active players by clicking the "Start Active Players" button on the Yahoo Fantasy UI. Active means a player's team is playing on the corresponding date.

4 cases where the report will tell the user to investigate their roster:
1. When an active player is on the bench. This will only occur if more than 10 players are active for that day.
2. When an active player's status is Injured
3. When an active player's status is Out
4. When an active player's status is GTD

If any of these 4 situations occur, then it is in the user's best interest to manually set up their roster for that day because the "Start Active Players" button may have produced undesired results.

Note:
1. The default number of days that the script will automate is set to 7 days. Feel free to change the number in the source code as the user sees fit.
2. This script assumes the user is only enrolled in ONE Yahoo Fantasy League. I have not accounted for multiple leagues
3. This script assumes the user has 13 players. I have not accounted for 14 players if the user has an injured player

## Dependencies
* [Python 3.5](https://www.python.org/downloads/release/python-350/)
* [Selenium WebDriver](http://www.seleniumhq.org/download/)
* [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads). Additionally check out their ["Getting started page"](https://sites.google.com/a/chromium.org/chromedriver/getting-started) 

## Setup
1. Download script
2. Install dependencies
3. Change CHROME_DRIVER_PATH to the location of your chromedriver.exe file if necessary.
4. Change NUM_OF_PLAYERS and NUM_OF_DAYS variable as necessary
5. Run Program

## Example Output

Below is an example of a report for a given day generated by the script. The left window is Yahoo's Fantasy Basketball website while the right window is my terminal on Ubuntu.

![alt text](/examples/report.png)

I could not screenshot all of the printouts by the terminal for that day but it does capture every single player from the roster on the left I promise. For the above screenshot I have 2 windows open. On the left is the Yahoo Fantasy roster and on the right is my Ubuntu terminal that is outputting results from my Python script. In the terminal the first thing you see is the date. On the website on the upper left corner you can see the corresponding date.

As you can see for each player in the terminal, 5 attributes are displayed:
1. Player Name
2. Player's team and list of Fantasy Basketball positions that player can be assigned to 
3. Player's current assigned Fantasy Basketball position
4. Player's opponent
5. Player's Status (Healthy, Injured, Game Time Decision (GTD), or Out)

The order that the terminal outputs each player is the same order that they appear on your Yahoo Fantasy roster

So if we take the first person on my fantasy team, D'Angelo Russell:
1. D'Angelo Russell
2. Bkn which is short for Brooklyn Nets. Russell can play either PG, SG, and technically G as well (G position means either SG or PG are eligible) 
3. Russell is assigned to the PG Fantasy Basketball position
4. He is playing against Pho (Phoneix Suns). The @ symbol means he is a visitor so he is playing at Pho's arena. Note that the next player in my roster, Devin Booker, plays for Pho and is playing against Bkn without an @ symbol therefore Booker is playing at his home arena in Pho.
5. No alarming statuses detected on the UI so the terminal outputs that he is Healthy

Each of the attributes are web scraped via Selenium by looking at the Yahoo's website's various web elements.

![alt text](/examples/report2.png)

Above is an example of what the report outputs at the end of the script when at least one of the 4 situations I outlined in the [description](#description) occur.

In specific, situations 1, 2, and 4 are occuring. For situation 1 am showing my roster for the date of November 22'nd (date is displayed in the upper left corner). The "Start Active Players" button ended up benching one of my best players on my roster Devin Booker. I'm not sure what the algorithm is that Yahoo implemented by thanks to the script I am notified that Devin Booker got benched even though he has a game that day. I definitely would start him 100% of the time over Courtney Lee so I will have to manually change my roster for that day. For situation 2 and 4 you can see that D'Angelo Russell is marked as Injured but has a game that day and Anthony Davis is marked as GTD but has a game that day.

## To-Do List

- [x] Capability of creating a report for x number of days
- [x] Report status of a player e.g. Healthy, Injured, Out, Game Time Decision(GTD)
- [x] Have the report mention if any Benched, Injured, Out, and GTD players are Active
- [x] Have the script prompt the user for their yahoo email, password, and team name instead of editing the source code
- [ ] Additional Exception handling
- [ ] Remove print statements and implement logging practices
- [ ] Implement [Page Object Model](https://www.toptal.com/selenium/test-automation-in-selenium-using-page-object-model-and-page-factory) to practice code maintainability and loose coupling coding practices.


**[Return to Table of Contents](#table-of-contents)**