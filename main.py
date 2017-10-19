from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
		print(active_bench_list[x][0] + " " + active_bench_list[x][1])

def start_active_players(driver):
	print("Starting active players...")
	driver.find_element_by_xpath("//*[contains(text(), 'Start Active Players')]").click()	

def click_next_date(driver):
	driver.find_element_by_xpath("//a[@class='Js-next Grid-u No-bdr-radius-start No-bdrstart Pstart-med Td-n Fz-xs ']/span").click() 

def main():
#Required setup to access Yahoo Fantasy Basketball. Change capitilized variables as needed
	URL = 'https://basketball.fantasysports.yahoo.com/'
	YAHOO_EMAIL = 'xxxxxxx'
	YAHOO_PASSWORD = 'xxxxxxx'
	TEAM_NAME = 'The Clinic'
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
	
	for day in range(0,NUM_OF_DAYS):
		date = driver.find_element_by_xpath("//span[@id='selectlist_nav']/a[2]").text
		print("Date is: " + date + "\n")
		start_active_players(driver)
		
		for x in range(1,NUM_OF_PLAYERS+1):
		#tr[x] where x is the x'th player row. First element is 1 NOT 0
			player_name_team_base_xpath = "//table/tbody/tr[" + str(x)+ "]"
			player_name_xpath = player_name_team_base_xpath + "/td[3]/div/div/div/a"
			player_team_xpath = player_name_team_base_xpath + "/td[3]/div/div/div/span"
			player_position_xpath = player_name_team_base_xpath +"/td[1]/div/span"
			player_opponent_xpath = player_name_team_base_xpath + "/td[5]/div"
			player_name = driver.find_element_by_xpath(player_name_xpath).text
			player_team = driver.find_element_by_xpath(player_team_xpath).text
			player_position = driver.find_element_by_xpath(player_position_xpath).text
			player_opponent = driver.find_element_by_xpath(player_opponent_xpath).text
			print('Player: ', player_name)
			print('Team: ', player_team)
			print('Fantasy Basketball Position: ', player_position)
			if not player_opponent:
				print(player_name + ' is not playing today')
			else: # Player is active
				print('Opponent: ', player_opponent)
				if player_position == 'BN':
					active_bench_list.append([date, player_name])
			print()
		
		if active_bench_list:
			print()
			print_active_bench_players(active_bench_list)

		click_next_date(driver)

#Shutdown
	input('Enter any key to exit')
	driver.close()

if __name__ == "__main__":
	main()