from selenium import webdriver
import pandas as pd
import time


file_path = "../data/Liste_mails_retargeting.xlsx"
chromedriver_path = "/Users/basileroth/Desktop/Work/Extra/email_insta/chromedriver"
name_column_mail = "Mail"
name_column_status = "Inscrit sur Insta"



# Load the xlsx file
df = pd.read_excel(file_path)

# Test data
email_list = ['basileroth.75@gmail.com','basidsdsdleroth.75@gmail.com']

# Downloaded from http://chromedriver.storage.googleapis.com/index.html?path=81.0.4044.69/
# You have to get the chromdriver version similar to your real chrome version
# Load the driver
driver = webdriver.Chrome(chromedriver_path)

# Open the website
driver.get('https://www.instagram.com/accounts/emailsignup/')
time.sleep(1) # Wait to load

for index, row in df.iterrows():

	start_time = time.time() # Start the timer
	exist = "" # False = No insta account | True = Insta account exists
	time.sleep(1) # Wait to load

	# To get the 2 needed boxes
	box_email = driver.find_element_by_name('emailOrPhone')
	box_under = driver.find_element_by_name('fullName')

	# Write the email in the email box
	box_email.send_keys(row[name_column_mail])

	# Select the box under to make the X or V 
	box_under.click()
	time.sleep(1) # Wait to load

	# Check the name of the new element in the box 
	elem = driver.find_element_by_class_name("i24fI").find_element_by_tag_name("span")
	if elem.get_attribute("class")  == "coreSpriteInputError gBp1f":
		exist = "Oui"
	elif elem.get_attribute("class")  == "coreSpriteInputAccepted gBp1f":
		exist = "Non"

	df[name_column_status][index] = exist
	print(row[name_column_mail] + " : " + exist)

	end_time = time.time() # End the timer
	print("Time : ",str((end_time-start_time)*1000.0) ," ms")
	driver.refresh() # Refresh the page to erase written data

# Save the result to the liste_mail_output
df.to_excel("../output/liste_mail_output.xlsx")  

