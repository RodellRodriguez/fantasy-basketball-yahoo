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

def main():
#Look up how to install chromedriver	
	chrome_driver_path = "/usr/local/bin/chromedriver"
	options = webdriver.ChromeOptions()
	options.add_argument('--start-maximized')
	driver = webdriver.Chrome(executable_path= chrome_driver_path, chrome_options=options)
	yahoo_email = 'xxxxxxx'
	yahoo_password = 'xxxxx'
	team_name = 'xxxxx'

	driver.get('https://basketball.fantasysports.yahoo.com/')
	driver.find_element_by_id('yucs-profile').click()
	explicit_wait_by_id(driver,'login-username').send_keys(yahoo_email)
	driver.find_element_by_id('login-signin').click()
	explicit_wait_by_id(driver,'login-passwd').send_keys(yahoo_password)
	driver.find_element_by_id('login-signin').click()

	element = explicit_wait_by_link_text(driver,team_name)
	print('Team name is: ' + element.text)
	element.click()

	date = driver.find_element_by_xpath("//span[@id='selectlist_nav']/a[2]")
	print("Date is: " + date.text + "\n")

#Doing this manually for each player just to get it working. Will incorporate a for loop
#tr[x] where x is the x'th row. First element is 1 NOT 0
	player_name_team_base_xpath = "//table/tbody/tr[1]"
	player_name_xpath = player_name_team_base_xpath + "/td[3]/div/div/div/a"
	player_team_xpath = player_name_team_base_xpath + "/td[3]/div/div/div/span"
	player_position_xpath = player_name_team_base_xpath +"/td[1]/div/span"
	player_opponent_xpath = player_name_team_base_xpath + "/td[4]/div"
	player_name = driver.find_element_by_xpath(player_name_xpath).text
	player_team = driver.find_element_by_xpath(player_team_xpath).text
	player_position = driver.find_element_by_xpath(player_position_xpath).text
	player_opponent = driver.find_element_by_xpath(player_opponent_xpath).text
	print('Player: ', player_name)
	print('Team: ', player_team)
	print('Fantasy Basketball Position: ', player_position)
	if not player_opponent:
		print(player_name + ' is not playing today')
	else:
		print('Opponent: ', player_opponent)

	print("\n")

#tr[x] where x is the x'th row. First element is 1 NOT 0
	player_name_team_base_xpath = "//table/tbody/tr[4]"
	player_name_xpath = player_name_team_base_xpath + "/td[3]/div/div/div/a"
	player_team_xpath = player_name_team_base_xpath + "/td[3]/div/div/div/span"
	player_position_xpath = player_name_team_base_xpath +"/td[1]/div/span"
	player_opponent_xpath = player_name_team_base_xpath + "/td[4]/div"
	player_name = driver.find_element_by_xpath(player_name_xpath).text
	player_team = driver.find_element_by_xpath(player_team_xpath).text
	player_position = driver.find_element_by_xpath(player_position_xpath).text
	player_opponent = driver.find_element_by_xpath(player_opponent_xpath).text
	print('Player: ', player_name)
	print('Team: ', player_team)
	print('Fantasy Basketball Position: ', player_position)
	if not player_opponent:
		print(player_name + ' is not playing today')
	else:
		print('Opponent: ', player_opponent)

	print("\n")




	input('Enter any key to exit')
	driver.close()

if __name__ == "__main__":
	main()