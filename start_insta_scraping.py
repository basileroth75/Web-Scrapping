"""
A simple selenium test example written by python
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

##############################################
##### Modify the name of the file here #######
name_file = "Liste_mails_retargeting.xlsx"
##############################################
## NAME OF THE COLUMN WHERE THE EMAILS ARE ###
name_column_mail = "Mail"
##############################################
## NAME OF THE COLUMN OF THE DESIRED OUTPUT ##
name_column_status = "Inscrit sur Insta"



file_path = "docker-python-chromedriver/data/" + name_file


class WebChromeDriver():

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(2)

    def tearDown(self):
        """Stop web driver"""
        print("Quitting")
        self.driver.quit()


if __name__ == '__main__':


    chrome_driver = WebChromeDriver()
    chrome_driver.driver.get('https://www.instagram.com/accounts/emailsignup/')
    df = pd.read_excel(file_path)
    time.sleep(1) 

    for index, row in df.iterrows():

        start_time = time.time() # Start the timer
        exist = "" # False = No insta account | True = Insta account exists
        time.sleep(1) # Wait to load

        # To get the 2 needed boxes
        box_email = chrome_driver.driver.find_element_by_name('emailOrPhone')
        box_under = chrome_driver.driver.find_element_by_name('fullName')

        # Write the email in the email box
        box_email.send_keys(row[name_column_mail])

        # Select the box under to make the X or V 
        box_under.click()
        time.sleep(2) # Wait to load

        # Check the name of the new element in the box 
        elem = chrome_driver.driver.find_element_by_class_name("i24fI").find_element_by_tag_name("span")
        if elem.get_attribute("class")  == "coreSpriteInputError gBp1f":
            exist = "Oui"
        elif elem.get_attribute("class")  == "coreSpriteInputAccepted gBp1f":
            exist = "Non"

        df[name_column_status][index] = exist
        print(row[name_column_mail] + " : " + exist)

        end_time = time.time() # End the timer
        print("Time : ",str((end_time-start_time)*1000.0) ," ms")
        chrome_driver.driver.refresh() # Refresh the page to erase written data


    # Save the result to the liste_mail_output
    chrome_driver.tearDown()
    df.to_excel("liste_mail_output.xlsx")  
    print("Saved")
