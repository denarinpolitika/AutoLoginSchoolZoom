import selenium #Selenium with Python is used to carry out automated test cases for browsers or web applications
import time
import schedule
from selenium import webdriver #Webdriver is the parent of all methods and classes used in Selenium Python
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

email="insert.email@gmail.com" #University email address
password="Insert_password_here" #University email password


path="C:/Users/Name/OneDrive/Desktop/Chromedriver.exe" #Path to browser driver (Chrome)
driver=webdriver.Chrome(path)
driver.get("https://SCHOOL.zoom.us/signin") #Get Zoom webpage

driver.find_element(By.XPATH, '/html/body/div/form/p[1]/input').send_keys(email) #Insert email in zoom webpage
driver.find_element(By.XPATH, '/html/body/div/form/p[2]/input').send_keys(password) #Insert password in zoom webpage
login_loc='/html/body/div/form/p[3]/input'
logbutton = driver.find_elements_by_xpath(login_loc)[0] #Find login button
logbutton.click() #Click login button

priv_loc='/html/body/div/div[3]/form[1]/input'
privbutton = driver.find_elements_by_xpath(priv_loc)[0]
privbutton.click()

 
driver.get('https://SCHOOL.zoom.us/j/92986585721?pwd=K0l0VmFqeVh0emtxZjNVMGEwZWpQZz09&uname=Name%20Surname#success') #Get zoom link for specific lesson
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("insert.email@gmail.com") #Insert email in zoom webpage
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("MInsert_password_here") #Insert password in zoom webpage
login_button = driver.find_elements_by_xpath('//*[@id="loginbtn"]')[0] #Find login button
login_button.click() #Click button







