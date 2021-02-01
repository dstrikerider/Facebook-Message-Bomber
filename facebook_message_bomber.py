from selenium import webdriver
import time

print('\t\tMessage Bomber for Facebook-Messenger')
print('\tDeveloped By Debshubra Chakraborty (Strike Rider)\n')

#Getting Nessesary Inputs from User

email_id = input('Enter Username : ')
password = input('Enter Password : ')
message = input('Enter Message : ')
search_input = input('Enter Contact Name : ')
iterator = int(input('Enter Number of Iterations : '))

#Creating Webdriver
test_webdriver = webdriver.Firefox() 

#Opening Facebook Messenger
test_webdriver.get('https://www.facebook.com/messages/t/100019720792604/')

#Giving Login Credentials & Attempting Login
email_arg = test_webdriver.find_element_by_id('email')
password_arg = test_webdriver.find_element_by_id('pass')
login_button = test_webdriver.find_element_by_id('loginbutton')
email_arg.send_keys(email_id)
password_arg.send_keys(password)
login_button.click()

time.sleep(10)

#Giving Inuputs In Searchbar
search_bar = test_webdriver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/label/input')
search_bar.send_keys(search_input)

time.sleep(10)

#Taking The First Seach Result
search_bar_first_result = test_webdriver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/ul/div/li/div/a/div')
search_bar_first_result.click()

time.sleep(10)

#Giving Message Input & Sending
message_box = test_webdriver.find_element_by_css_selector('.notranslate')
for i in range(0, iterator):
    message_box.send_keys(message)
    send_button = test_webdriver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]')
    send_button.click()

time.sleep(5)

#Closing the Webdriver

test_webdriver.close()
print('\n\t\tThanks for using.')