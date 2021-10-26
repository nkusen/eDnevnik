import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from statistics import mean

myUsername = input("Username: ")
myPassword = input("Password: ")

PATH = os.path.dirname(os.path.realpath(__file__)) + "\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(PATH, options=options)

driver.get("https://ocjene.skole.hr/login")
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
btn = driver.find_element_by_css_selector('.form-login > input[type="submit"]')

username.send_keys(myUsername)
password.send_keys(myPassword)
btn.send_keys(Keys.RETURN)

predmeti = driver.find_elements_by_css_selector(".list > li > a")
for i in range(len(predmeti)):
    predmeti = driver.find_elements_by_css_selector(".list > li > a")
    predmet = predmeti[i]

    print(predmet.find_element_by_tag_name("span").text)
    predmet.send_keys(Keys.RETURN)
    
    ocjene = [int(ocj.text) for ocj in driver.find_elements_by_class_name("positive")]
    if len(ocjene) > 0:
        print(mean(ocjene))
    else:
        print("Nema unesenih ocjena!")

    driver.back()

driver.quit()

input("Press enter to exit...")
