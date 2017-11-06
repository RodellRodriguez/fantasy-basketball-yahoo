#getpass is a secure way for people to input their password without it displaying on the terminal
import getpass
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException


def explicit_wait_by_id(driver, id):
	element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, id)))
	return element

def explicit_wait_by_link_text(driver, link_text):
	element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, link_text)))
	return element

def explicit_wait_by_xpath(driver, xpath):
	element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))
	return element	

#Each element of the list will be a list of 2 elements: Date and Player Name
def print_active_bench_players(active_bench_list):
	print('Players who are playing but are assigned to the bench:')
	for x in range(0,len(active_bench_list)):
		print(active_bench_list[x][0] 
			+ ", " + active_bench_list[x][1])

#Each element of the list will be a list of 3 elements: Date, Player Name, and their Status
def print_active_ineligible_status_players(active_ineligible_status_list):
	print('Players who are playing but might not play:')
	for x in range(0,len(active_ineligible_status_list)):
		print(active_ineligible_status_list[x][0] 
			+ ", " + active_ineligible_status_list[x][1] 
			+ ", " + active_ineligible_status_list[x][2])	

def start_active_players(driver):
	print("Starting active players...")
	driver.find_element_by_xpath("//*[contains(text(), 'Start Active Players')]").click()	

def click_next_date(driver):
	print("Clicking next date...")
	driver.find_element_by_xpath("//a[@class='Js-next Grid-u No-bdr-radius-start No-bdrstart Pstart-med Td-n Fz-xs ']/span").click() 

def get_email():
	prompt = 'Please enter yahoo email. You do not need to input @yahoo.com:\n'
	while True:
		email = input(prompt)
		prompt_confirmation = 'Re-enter your email for confirmation\n'
		email_confirmation = input(prompt_confirmation)
		if email == email_confirmation: 
			return email
		else:
			print('Emails do not match. Try again.') 

def get_password():
	prompt = 'Please enter yahoo password:\n'
	while True:
		password = getpass.getpass(prompt)
		prompt_confirmation = 'Re-enter your password for confirmation\n'
		password_confirmation = getpass.getpass(prompt_confirmation)
		if password == password_confirmation: 
			return password
		else:
			print('Passwords do not match. Try again.')

def get_team_name():
	prompt = 'Please enter the exact name of your team:\n'
	while True:
		team_name = input(prompt)
		prompt_confirmation = 'Re-enter your team name for confirmation\n'
		team_name_confirmation = input(prompt_confirmation)
		if team_name == team_name_confirmation: 
			return team_name
		else:
			print('Team names do not match. Try again.')

def main():
#Required setup to access Yahoo Fantasy Basketball. Change capitilized variables as needed
	URL = 'https://basketball.fantasysports.yahoo.com/'
	YAHOO_EMAIL = get_email()
	YAHOO_PASSWORD = get_password()
	TEAM_NAME = get_team_name()
	NUM_OF_PLAYERS = 13
	NUM_OF_DAYS = 7 

	CHROME_DRIVER_PATH = "/usr/local/bin/chromedriver"
	OPTIONS = webdriver.ChromeOptions()
	OPTIONS.add_argument('--start-maximized')
	driver = webdriver.Chrome(executable_path= CHROME_DRIVER_PATH, chrome_options=OPTIONS)

#Login Procedure
	driver.get(URL)
	driver.find_element_by_id('yucs-profile').click()
	explicit_wait_by_id(driver,'login-username').send_keys(YAHOO_EMAIL)
	driver.find_element_by_id('login-signin').click()
	explicit_wait_by_id(driver,'login-passwd').send_keys(YAHOO_PASSWORD)
	driver.find_element_by_id('login-signin').click()

#Navigate to My Players
	element = explicit_wait_by_link_text(driver,TEAM_NAME)
	print('Team name is: ' + element.text)
	element.click()

#Getting Player Information
	active_bench_list = []
	active_ineligible_status_list = []
	
	for day in range(0,NUM_OF_DAYS):
		print('*' * 50)
		date = driver.find_element_by_xpath("//span[@id='selectlist_nav']/a[2]").text
		print("Date is: " + date)
		start_active_players(driver)
		
		for x in range(1,NUM_OF_PLAYERS+1):
		#tr[x] where x is the x'th player row. First element is 1 NOT 0
			print()
			player_name_team_base_xpath = "//table/tbody/tr[" + str(x)+ "]"
			player_name_xpath = player_name_team_base_xpath + "/td[3]/div/div/div/a"
			player_team_xpath = player_name_team_base_xpath + "/td[3]/div/div/div/span"
			player_position_xpath = player_name_team_base_xpath +"/td[1]/div/span"
			player_opponent_xpath = player_name_team_base_xpath + "/td[5]/div"
			player_status_xpath = player_name_team_base_xpath + "/td[3]/div/div[2]/span"
			
			attempts = 0
			while attempts < 3:
				try:
					player_name = driver.find_element_by_xpath(player_name_xpath).text
					player_team = driver.find_element_by_xpath(player_team_xpath).text
					player_position = driver.find_element_by_xpath(player_position_xpath).text
					player_opponent = driver.find_element_by_xpath(player_opponent_xpath).text
					player_status = driver.find_element_by_xpath(player_status_xpath).text
					break
				except StaleElementReferenceException as e:
					pass
				attempts += 1

		#If we receive an empty string
			if not player_status: 
				player_status = 'Healthy'
		#Start printing player information
			print('Player: ', player_name)
			print('Team: ', player_team)
			print('Fantasy Basketball Position: ', player_position)
			if player_opponent:
				print('Opponent: ', player_opponent)
			#Check the 4 Cases and notify user if any of them occur
				if player_position == 'BN': 
					active_bench_list.append([date, player_name])
				if player_status == 'Injured' or \
					player_status == 'Out' or \
					player_status == 'GTD': 
						active_ineligible_status_list.append([date, player_name, player_status])
			else: 
				print(player_name + ' is not playing today')
			print('Status: ', player_status)

		try:
			click_next_date(driver)
		except WebDriverException as e:
			raise e
			driver.refresh()
			click_next_date(driver)
		
#Print report	
	if active_bench_list:
		print()
		print_active_bench_players(active_bench_list)
	if active_ineligible_status_list:
		print()
		print_active_ineligible_status_players(active_ineligible_status_list)

#Shutdown
	input('Enter any key to exit')
	driver.close()

if __name__ == "__main__":
	main()